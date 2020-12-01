from global_hotkeys import *

import time

# Flag to indicate the program whether should continue running.
is_alive = True

def print_hello():
    print("Hello")

def print_world():
    print("World")

def exit_application():
    global is_alive
    stop_checking_hotkeys()
    is_alive = False

# Declare some key bindings.
bindings = [
    [["control", "shift", "7"], None, print_hello],
    [["control", "shift", "8"], None, print_world],
    [["control", "shift", "9"], None, exit_application],
]

# Register all of our keybindings
register_hotkeys(bindings)

# Finally, start listening for keypresses
start_checking_hotkeys()

# Keep waiting until the user presses the exit_application keybinding.
# Note that the hotkey listener will exit when the main thread does.
while is_alive:
    time.sleep(0.1)