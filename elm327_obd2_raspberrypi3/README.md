# ELM327 Vehicle Data via python-OBD

This project connects a Raspberry Pi (or Linux system) to an ELM327 adapter to read real-time vehicle data using the OBD-II protocol.
🇬🇧 English – Overview and Usage
🚗 Project Overview

This project demonstrates how to connect a Raspberry Pi (or any Linux-based system) to a vehicle’s OBD-II interface using an ELM327 adapter (Bluetooth, USB, or WiFi). The connection allows you to read real-time engine data such as RPM, speed, coolant temperature, throttle position, and more using Python and the python-OBD library.
🔧 How It Works

    The ELM327 adapter is plugged into your vehicle's OBD-II port.

    The Raspberry Pi communicates with the ELM327 via Bluetooth (or optionally via USB/WiFi).

    The Python script queries the ECU using standard OBD-II PID commands.

    Live data is displayed in the terminal or optionally saved/logged.

🧰 Use Cases

    Diagnose engine performance in real-time

    Monitor RPM, temperature, and voltage

    Build a car dashboard using Raspberry Pi

    Educational tools for automotive electronics

    Remote diagnostics or data logging for fleet vehicles

    ✅ Works with most vehicles manufactured after 2001 (Europe) or 1996 (USA) that support OBD-II.

🇩🇪 Deutsch – Überblick und Verwendung
🚗 Projektübersicht

Dieses Projekt zeigt, wie man ein Raspberry Pi (oder ein anderes Linux-System) über einen ELM327-Adapter (Bluetooth, USB oder WLAN) mit dem OBD-II-Anschluss eines Fahrzeugs verbindet. Damit lassen sich in Echtzeit Fahrzeugdaten wie Drehzahl (RPM), Geschwindigkeit, Motortemperatur, Drosselklappenstellung usw. mit Python und der python-OBD-Bibliothek auslesen.
🔧 Funktionsweise

    Der ELM327-Adapter wird in die OBD-II-Schnittstelle des Fahrzeugs gesteckt.

    Das Raspberry Pi kommuniziert über Bluetooth (oder USB/WLAN) mit dem ELM327.

    Ein Python-Skript sendet OBD-II-Befehle (PIDs) an das Steuergerät.

    Die Fahrzeugdaten werden im Terminal angezeigt oder gespeichert.

🧰 Anwendungsmöglichkeiten

    Live-Diagnose von Fahrzeugdaten

    Überwachung von RPM, Temperatur und Spannung

    Bau eines digitalen Fahrzeug-Dashboards mit Raspberry Pi

    Lernprojekte im Bereich Automobilelektronik

    Fernwartung und Datenaufzeichnung in Flottenfahrzeugen

    ✅ Kompatibel mit den meisten Fahrzeugen ab Baujahr 2001 (Europa) bzw. 1996 (USA), die OBD-II unterstützen
## 🔌 Supported OBD-II Parameters (Based on Your Vehicle)

| Parameter Name            | OBD-II PID | Description                          |
|--------------------------|------------|--------------------------------------|
| RPM                      | 010C       | Engine Revolutions Per Minute        |
| SPEED                    | 010D       | Vehicle Speed (km/h)                 |
| COOLANT_TEMP             | 0105       | Engine Coolant Temperature (°C)      |
| THROTTLE_POS             | 0111       | Throttle Position (%)                |
| INTAKE_PRESSURE          | 010B       | Intake Manifold Pressure (kPa)       |
| INTAKE_TEMP              | 010F       | Intake Air Temperature (°C)          |
| MAF                      | 0110       | Mass Air Flow Rate                   |
| TIMING_ADVANCE           | 010E       | Ignition Timing Advance              |
| FUEL_STATUS              | 0103       | Current Fuel System Status           |
| CONTROL_MODULE_VOLTAGE   | 0142       | ECU Voltage Supply (V)               |

> ✅ These are supported on your Mazda when ignition is ON.

## 🛠 Usage Instructions

1. Run `elm327_connect.sh` to bind the ELM327 to `/dev/rfcomm0`
2. Run `python3 supported_cmd.py` to view available PIDs
3. Run `python3 read_obd_data.py` to start real-time monitoring

![SSH Logs](images/bt.png)
![schematic](images/elm327_pi3.jpg)

