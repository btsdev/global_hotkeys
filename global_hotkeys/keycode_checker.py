import keyboard

def on_key(event):
    if event.event_type == keyboard.KEY_DOWN:
        print("Key pressed:", event.name)
        print("VK Code: 0x{:02X}".format(event.scan_code))

keyboard.on_press(on_key)

print("Press any key (Ctrl+C to exit)")

# Block until Ctrl+C is pressed
keyboard.wait('esc')