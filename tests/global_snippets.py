from global_hotkeys import *

from datetime import datetime
import time
import win32api, win32con
import winsound

# pip install pyperclip
try:
    import pyperclip
except ImportError as e:
    raise("You need to install pyperclip to use this script.\nJust use 'pip install pyperclip'")

# Flag to indicate the program whether should continue running.
is_alive = True

snippets_allowed = False

def toggle_snippets():
    global snippets_allowed
    snippets_allowed = not snippets_allowed
    print("snippets enabled" if snippets_allowed else "snippets disabled")
    winsound.Beep(400, 10) if snippets_allowed else winsound.Beep(200, 10)

def print_world():
    print("World")

def exit_application():
    global is_alive
    print("exiting")
    stop_checking_hotkeys()
    is_alive = False

def press_backspace():
    win32api.keybd_event(0x08,0,0,0)
    time.sleep(0.05)
    win32api.keybd_event(0x08,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.05)

def press_control_v():
    win32api.keybd_event(0x11,0,0,0)
    time.sleep(0.05)
    win32api.keybd_event(0x56,0,0,0)
    time.sleep(0.05)
    win32api.keybd_event(0x56,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.05)
    win32api.keybd_event(0x11,0,win32con.KEYEVENTF_KEYUP,0)
    time.sleep(0.05)

def clear_chord_from_input_field(chord_length):
    for i in range(0, chord_length):
        press_backspace()

def paste_to_focused_input(str):
    old_clipboard_content = pyperclip.paste()
    pyperclip.copy(str)
    press_control_v()
    pyperclip.copy(old_clipboard_content)

def print_test():
    global snippets_allowed
    if not snippets_allowed:
        return
    clear_chord_from_input_field(2)
    date_string = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    paste_to_focused_input(date_string)

# Declare some key bindings.
bindings = [
    ["control + shift + z", None, toggle_snippets, False],
    ["t,m", None, print_test, False],
]

# Register all of our keybindings
register_hotkeys(bindings)

# Finally, start listening for keypresses
start_checking_hotkeys()

# Keep waiting until the user presses the exit_application keybinding.
# Note that the hotkey listener will exit when the main thread does.
while is_alive:
    time.sleep(0.1)