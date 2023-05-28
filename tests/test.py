from global_hotkeys import *

import time

# Flag to indicate the program whether should continue running.
is_alive = True

def print_hello():
    print("Hello")

def print_world():
    print("World")

def print_foo():
    print("Foo")

def print_bar():
    print("Bar")

def exit_application():
    global is_alive
    print("exiting")
    stop_checking_hotkeys()
    is_alive = False


# Declare some key bindings.
bindings = [
    ["control + 7, control + 4", None, print_world, True],
    ["control + 5", None, print_hello, False],
    ["window + 1", None, print_foo, False],
    ["t,m", None, print_bar, False],
    ["control + Q", None, exit_application, False],
]

# Register all of our keybindings
register_hotkeys(bindings)

# Finally, start listening for keypresses
start_checking_hotkeys()

# Keep waiting until the user presses the exit_application keybinding.
# Note that the hotkey listener will exit when the main thread does.
while is_alive:
    time.sleep(0.1)