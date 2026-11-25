#!/bin/bash
# Pair the adapter with bluetoothctl first; this script only creates the binding.
set -eu
if [ "$#" -ne 1 ] || ! [[ "$1" =~ ^([[:xdigit:]]{2}:){5}[[:xdigit:]]{2}$ ]]; then
    echo "Usage: $0 <ADAPTER_MAC>" >&2
    exit 2
fi
if [ -e /dev/rfcomm0 ]; then
    echo "/dev/rfcomm0 already exists; check its owner before changing it." >&2
    exit 1
fi
sudo rfcomm bind rfcomm0 "$1"
if [ -e /dev/rfcomm0 ]; then
    echo "/dev/rfcomm0 is available."
else
    echo "Binding did not create /dev/rfcomm0; check Bluetooth and system logs." >&2
    exit 1
fi
