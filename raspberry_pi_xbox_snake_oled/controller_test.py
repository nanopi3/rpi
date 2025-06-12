from inputs import get_gamepad

print("🎮 Waiting for Xbox 360 controller input...\n(Press Ctrl+C to quit)")

try:
    while True:
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Key" and event.state == 1:
                print(f"🔘 Button Pressed: {event.code}")
            elif event.ev_type == "Absolute":
                print(f"🎮 Movement: {event.code} = {event.state}")
except KeyboardInterrupt:
    print("\n🛑 Exit.")
