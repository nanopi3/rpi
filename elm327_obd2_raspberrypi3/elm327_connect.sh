#!/bin/bash

# Bluetooth MAC address of your ELM327 adapter
MAC="00:1D:A5:68:98:8A"

echo "🔄 Restarting Bluetooth service..."
sudo systemctl restart bluetooth
sleep 2

echo "❌ Removing old pairing (if exists)..."
echo -e "remove $MAC\nexit" | bluetoothctl > /dev/null

echo "🔍 Scanning and pairing ELM327..."
echo -e "scan on\npair $MAC\ntrust $MAC\nconnect $MAC\nexit" | bluetoothctl
sleep 3

echo "🔌 Releasing existing rfcomm0 (if any)..."
sudo rfcomm release rfcomm0 > /dev/null 2>&1

echo "🔗 Binding rfcomm0 to $MAC ..."
sudo rfcomm bind rfcomm0 $MAC

# Final check
if [ -e /dev/rfcomm0 ]; then
    echo "✅ /dev/rfcomm0 is ready. You can now use it in Python."
else
    echo "❌ Connection failed. Please check Bluetooth and ignition status."
fi
