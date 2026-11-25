# ELM327 vehicle data on Raspberry Pi

[Deutsch](README.de.md)

This experiment reads OBD-II commands through a Bluetooth ELM327-compatible adapter on a Raspberry Pi running Linux. `read_obd_data.py` queries the vehicle repeatedly with [python-OBD](https://python-obd.readthedocs.io/); `supported_cmd.py` lists commands detected by the library. The scripts use `/dev/rfcomm0`.

## Requirements

- Raspberry Pi 3 and Bluetooth ELM327-compatible adapter, as documented in the original project; other hardware is not verified here.
- A vehicle and adapter that support the requested OBD-II commands. Availability varies by vehicle, ignition state and adapter.
- Linux with BlueZ, `bluetoothctl` and `rfcomm`, plus Python 3, `python-OBD` (`obd`) and `colorama`.

On a Debian-based Raspberry Pi OS, install the OS packages and create an environment:

```bash
sudo apt update
sudo apt install bluetooth bluez python3-venv
python3 -m venv .venv
. .venv/bin/activate
python -m pip install obd colorama
```

Package availability and Bluetooth permissions depend on your OS version. Do not operate the computer while driving.

## Pair and connect

Connect the adapter to the vehicle and enable its ignition as required by the adapter. Find **your own adapter address** with `bluetoothctl`:

```text
bluetoothctl
power on
agent on
default-agent
scan on
```

After discovery, turn scanning off and replace `<ADAPTER_MAC>` below with the Bluetooth address reported for your adapter. Complete any pairing prompt required by the adapter.

```text
scan off
pair <ADAPTER_MAC>
trust <ADAPTER_MAC>
connect <ADAPTER_MAC>
quit
```

Bind the serial device (check first that `/dev/rfcomm0` is not already in use):

```bash
sudo rfcomm bind rfcomm0 <ADAPTER_MAC>
```

Alternatively, `./elm327_connect.sh <ADAPTER_MAC>` checks the address and refuses to overwrite an existing `/dev/rfcomm0`. Pairing is a separate manual step. The command may require sudo and Bluetooth access. Release the binding with `sudo rfcomm release rfcomm0` when you have finished, provided it is not being used by another application.

## Run

From this directory, with the environment active:

```bash
python supported_cmd.py
python read_obd_data.py
```

The reader prints a label and value when a query succeeds, or `Not available` for an unsupported or empty response. The code requests RPM, speed, coolant temperature, control-module voltage, throttle position, engine load, intake pressure and temperature, mass airflow, timing advance and fuel-system status. This is a list of **queries attempted by the code**, not a guarantee that a vehicle supports them.

## Troubleshooting

- Check `systemctl status bluetooth`, `bluetoothctl devices` and `ls -l /dev/rfcomm0`.
- Check the adapter's pairing instructions, ignition state, Bluetooth range and serial-device permissions.
- If a serial binding is stale, first identify the application using it; release it only when safe. Do not kill Bluetooth processes blindly.
- A connected adapter does not imply that every PID is available. Run `supported_cmd.py` to inspect the detected set.

![ELM327 adapter and Raspberry Pi wiring](images/elm327_pi3.jpg)

The examples have not been retested on physical hardware for this update.
