import obd

# Connect to the ELM327 adapter (Bluetooth)
connection = obd.OBD("/dev/rfcomm0", fast=False)

print("\n📡 Supported OBD-II Commands From Vehicle:\n")

supported_commands = connection.supported_commands

for cmd in supported_commands:
    print(f"{cmd.name} - {cmd}")
