# ELM327-Fahrzeugdaten auf dem Raspberry Pi

[English](README.md)

Dieses Experiment liest OBD-II-Daten über einen Bluetooth-ELM327-Adapter und `python-OBD`. Die Skripte erwarten `/dev/rfcomm0`. Die vorhandene Dokumentation nennt Raspberry Pi 3 und einen Bluetooth-Adapter; Kompatibilität und verfügbare Befehle hängen von Fahrzeug, Adapter und Betriebssystem ab.

## Installation und Verbindung

Auf einem Debian-basierten Raspberry Pi OS:

```bash
sudo apt update
sudo apt install bluetooth bluez python3-venv
python3 -m venv .venv
. .venv/bin/activate
python -m pip install obd colorama
bluetoothctl
```

In `bluetoothctl` Bluetooth aktivieren, mit `scan on` den eigenen Adapter suchen, mit `scan off` die Suche beenden und anschließend `pair <ADAPTER_MAC>`, `trust <ADAPTER_MAC>` und `connect <ADAPTER_MAC>` ausführen. `<ADAPTER_MAC>` durch die tatsächlich angezeigte Adresse ersetzen und eventuelle Kopplungsabfragen beantworten.

Wenn `/dev/rfcomm0` noch nicht verwendet wird:

```bash
sudo rfcomm bind rfcomm0 <ADAPTER_MAC>
python supported_cmd.py
python read_obd_data.py
```

Alternativ prüft `bash elm327_connect.sh <ADAPTER_MAC>` die Adresse und belegt keine bereits vorhandene `/dev/rfcomm0`-Schnittstelle. Die Kopplung erfolgt separat.

## Fehlersuche und Grenzen

`systemctl status bluetooth`, `bluetoothctl devices` und `ls -l /dev/rfcomm0` zeigen den lokalen Zustand. Zündung, Kopplung und Zugriffsrechte prüfen. Prozesse nicht pauschal beenden. Eine nicht mehr benötigte RFCOMM-Bindung kann nach Prüfung mit `sudo rfcomm release rfcomm0` gelöst werden.

Das Programm fragt unter anderem Drehzahl, Geschwindigkeit und Kühlmitteltemperatur ab; nicht jedes Fahrzeug unterstützt jeden Befehl. `supported_cmd.py` zeigt die vom Adapter erkannten Befehle. Das System nicht während der Fahrt bedienen. Für diese Dokumentationsänderung wurde kein Hardwaretest durchgeführt.
