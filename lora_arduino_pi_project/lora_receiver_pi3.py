import time
from LoRaRF import SX127x

# Create a LoRa object for SX127x modules
LoRa = SX127x()

# Set LoRa pins: NSS=GPIO8, RESET=GPIO22, DIO0=GPIO4
LoRa.setPins(8, 22, 4)

# Set SPI port: bus=0, cs=0, speed=7.8MHz
LoRa.setSpi(0, 0, 7800000)

# Initialize LoRa module
if not LoRa.begin():
    print("❌ LoRa init failed")
    exit()
print("✅ LoRa init successful")

# Configure LoRa modem settings
LoRa.setFrequency(433000000)
LoRa.setLoRaModulation(7, 125000, 5, False)
LoRa.setLoRaPacket(LoRa.HEADER_EXPLICIT, 12, 255, True, False)
LoRa.setTxPower(17, LoRa.TX_POWER_PA_BOOST)
LoRa.setRxGain(True, 6)
LoRa.setSyncWord(0x12)

LoRa.request()
print("📡 Listening for incoming LoRa packets...")

try:
    while True:
        LoRa.wait()
        if LoRa.available():
            payload = []
            while LoRa.available() > 0:
                payload.append(LoRa.read())
            message = bytes(payload).decode('utf-8', errors='ignore')
            print("📦 Received:", message)
            LoRa.request()
        time.sleep(0.1)
except KeyboardInterrupt:
    print("🛑 Exiting...")
