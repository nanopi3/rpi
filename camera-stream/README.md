# Raspberry Pi camera MJPEG stream

A Flask application captures frames with Picamera2, applies OpenCV filters and serves an MJPEG stream. The browser page offers normal, grayscale, Canny edge and Gaussian blur modes. The script initializes the camera at startup and requests a 640 × 480 video configuration.

## Requirements and setup

A Raspberry Pi with a Picamera2-compatible camera and a compatible Raspberry Pi OS installation is required. Picamera2 has system-level dependencies; follow the [Picamera2 installation instructions](https://github.com/raspberrypi/picamera2#installation) for your OS. The imports also require Flask, OpenCV, Pillow and NumPy. `requirements.txt` records the original Python dependencies; package installation can vary by OS and Python environment.

From this directory, after the camera and dependencies are configured:

```bash
python3 MJPEGStream.py
```

Visit `http://<raspberry-pi-ip>:5000/` from a trusted network. Stop the server with Ctrl+C.

## Limits and troubleshooting

- The development server listens on all interfaces and has **no authentication or TLS**. Use it only on a trusted network; do not expose it to the public internet without appropriate access controls.
- If startup fails, check camera detection, OS compatibility, permissions and the Picamera2 installation first. The camera is opened during module import, so this script is not suitable for hardware-free imports or CI tests as written.
- The existing dependency list has not been verified on current Raspberry Pi OS hardware.
