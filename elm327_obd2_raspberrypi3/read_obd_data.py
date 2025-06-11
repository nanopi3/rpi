import obd
import time
from colorama import Fore, Style, init

init(autoreset=True)

# Connect to ELM327
connection = obd.OBD("/dev/rfcomm0", fast=False)
if not connection.is_connected():
    print(Fore.RED + "❌ Connection to ELM327 failed. Ensure the car ignition is ON.")
    exit()

# Define all useful, supported commands
commands = {
    "Engine RPM": obd.commands.RPM,
    "Vehicle Speed (km/h)": obd.commands.SPEED,
    "Coolant Temp (°C)": obd.commands.COOLANT_TEMP,
    "ECU Voltage (V)": obd.commands.CONTROL_MODULE_VOLTAGE,
    "Throttle Position (%)": obd.commands.THROTTLE_POS,
    "Engine Load (%)": obd.commands.ENGINE_LOAD,
    "Intake Pressure (kPa)": obd.commands.INTAKE_PRESSURE,
    "Intake Air Temp (°C)": obd.commands.INTAKE_TEMP,
    "Mass Air Flow (g/s)": obd.commands.MAF,
    "Timing Advance (°)": obd.commands.TIMING_ADVANCE,
    "Fuel System Status": obd.commands.FUEL_STATUS
}

print(Fore.CYAN + "\n📡 Reading real-time vehicle data...\n(Press Ctrl+C to stop)\n")

try:
    while True:
        print(Style.BRIGHT + Fore.YELLOW + "-" * 60)
        for label, cmd in commands.items():
            response = connection.query(cmd)
            if response and not response.is_null():
                print(Fore.GREEN + f"{label}: {response.value}")
            else:
                print(Fore.RED + f"{label}: Not available")
        time.sleep(2)

except KeyboardInterrupt:
    print(Fore.MAGENTA + "\n🛑 Data reading stopped by user.")
