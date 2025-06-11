# GitHub: https://github.com/nanopi3

"""
English:
Live MJPEG video stream from Raspberry Pi Camera using Flask and Picamera2,
with selectable real-time filters (Normal, Grayscale, Edge Detection, Blur).

Deutsch:
Live-MJPEG-Videostream von der Raspberry Pi Kamera mit Flask und Picamera2,
mit auswählbaren Echtzeit-Filtern (Normal, Graustufen, Kantenerkennung, Weichzeichnen).
"""

from flask import Flask, Response, request
from picamera2 import Picamera2
from PIL import Image
import io
import time
import cv2
import numpy as np

app = Flask(__name__)

# Initialize the camera
picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
picam2.start()
time.sleep(1)

# Apply a filter to the frame
def apply_filter(frame, filter_type):
    if filter_type == 'gray':
        return cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    elif filter_type == 'edge':
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        return cv2.Canny(gray, 100, 200)
    elif filter_type == 'blur':
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        return cv2.GaussianBlur(gray, (5, 5), 0)
    else:
        # Normal mode → always return a copy
        return frame.copy()

# Generate MJPEG stream with selected filter
def generate(filter_type):
    while True:
        frame = picam2.capture_array()
        filtered = apply_filter(frame, filter_type)

        # Convert single-channel image (grayscale or edge) to RGB
        if len(filtered.shape) == 2:
            filtered = cv2.cvtColor(filtered, cv2.COLOR_GRAY2RGB)
        elif filtered.shape[2] == 4:
            filtered = cv2.cvtColor(filtered, cv2.COLOR_RGBA2RGB)

        img = Image.fromarray(filtered)
        buffer = io.BytesIO()
        img.save(buffer, format='JPEG')
        jpeg_data = buffer.getvalue()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpeg_data + b'\r\n')

# HTML page with filter selection buttons
@app.route('/')
def index():
    return '''
        <html>
            <head>
                <title>Live MJPEG Stream with Filters</title>
                <style>
                    button {
                        margin: 5px;
                        padding: 10px 20px;
                        font-size: 16px;
                        border-radius: 6px;
                    }
                </style>
                <script>
                    function setFilter(filter) {
                        document.getElementById("stream").src = "/video_feed?filter=" + filter;
                    }
                </script>
            </head>
            <body>
                <h1>Live Camera (MJPEG)</h1>
                <div>
                    <button onclick="setFilter('normal')">Normal</button>
                    <button onclick="setFilter('gray')">Grayscale</button>
                    <button onclick="setFilter('edge')">Edge Detection</button>
                    <button onclick="setFilter('blur')">Blur</button>
                </div>
                <img id="stream" src="/video_feed?filter=normal" width="640" height="480" />
            </body>
        </html>
    '''

# Video feed route that returns the filtered MJPEG stream
@app.route('/video_feed')
def video_feed():
    filter_type = request.args.get('filter', 'normal')
    return Response(generate(filter_type), mimetype='multipart/x-mixed-replace; boundary=frame')

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
