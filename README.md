# Raspberry Pi and embedded Linux experiments

Small Python and hardware experiments involving Raspberry Pi, cameras, Bluetooth OBD-II and LoRa. Each directory is independent; hardware and library versions matter, and the projects have not been validated on every current Raspberry Pi OS release.

| Project | Contents | Status |
| --- | --- | --- |
| [ELM327 OBD-II](elm327_obd2_raspberrypi3/) | Bluetooth serial connection and Python vehicle-data queries | Requires an ELM327 adapter and a compatible vehicle |
| [Camera stream](camera-stream/) | Flask MJPEG stream using Picamera2 and OpenCV filters | Requires a compatible Pi camera; the web server has no authentication |
| [LoRa receiver](lora_arduino_pi_project/) | Raspberry Pi SX127x receiver and an Arduino sender example | Prototype: library API and wiring need verification before use |
| [Controller and OLED experiment](raspberry_pi_xbox_snake_oled/) | Controller input example and OLED wiring notes | Snake game is a placeholder, not an implemented game |

Each project README describes its requirements, setup and limitations. The photographs in the project directories illustrate hardware setups; they are not automated test results. No physical hardware tests were run as part of this documentation update.

Maintained by [Ehsan Mohebbi](https://github.com/nanopi3). The repository has no declared license; ask the owner before reusing the code.
