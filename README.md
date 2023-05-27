# Python Global Hotkey Binding manager for Windows

Use this library to set system wide keybindings for your code to respond to.

## Installation

```
pip install global-hotkeys -U
```

## Example usage

```python
from global_hotkeys import *

import time

# Flag to indicate the program whether should continue running.
is_alive = True

# Our keybinding event handlers.
def print_hello():
    print("Hello")

def print_world():
    print("World")

def exit_application():
    global is_alive
    stop_checking_hotkeys()
    is_alive = False

# Declare some key bindings.
# These take the format of [<key list>, <keydown handler callback>, <keyup handler callback>]
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
```

## Additional functionality

You may also add/remove keybindings one at a time, in bulk, or completely clear them all out (which also stops the hotkey listener thread).

```python

# Just reusing our bindings declaration from above (this is not a complete code example, btw).
bindings = [
    [["control", "shift", "7"], None, print_hello],
    [["control", "shift", "8"], None, print_world],
    [["control", "shift", "9"], None, exit_application],
]

# Register a single keybinding (if it's not already registered). Returns True if the key didn't already exist and was added, else False (the binding is already registered - remove it first if you wish to overwrite it with new event handlers).
register_hotkey(bindings[0])

# Remove a single keybinding (if it exists). Returns True if the key existed and was removed, else False (the binding is already gone).
remove_hotkey(bindings[0])

# Register a list of keybindings.
register_hotkeys(bindings)

# Remove a list of keybindings.
remove_hotkeys(bindings)

# Remove all keybindings and terminate the hotkey listener thread.
clear_hotkeys()
```

## List of the available keys

```
backspace
tab
clear
enter
shift
control
alt
pause
caps_lock
escape
space   <-- a literal space character (' ') can be used as well.
page_up
page_down
left_window  <-- I couldn't get these to work on my keyboard (the microsoft docs say it's for microsoft natural keyboard?)
right_window <-- I couldn't get these to work on my keyboard (the microsoft docs say it's for microsoft natural keyboard?)
window       <-- I couldn't get these to work on my keyboard (the microsoft docs say it's for microsoft natural keyboard?)
end
home
left
up
right
down
select
print
execute
enter": win32con.VK_
print_screen
insert
delete
help
0
1
2
3
4
5
6
7
8
9
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
numpad_0
numpad_1
numpad_2
numpad_3
numpad_4
numpad_5
numpad_6
numpad_7
numpad_8
numpad_9
multiply_key
add_key
separator_key  <-- '|' also known as the 'pipe'
|
subtract_key
decimal_key
divide_key
f1
f2
f3
f4
f5
f6
f7
f8
f9
f10
f11
f12
f13
f14
f15
f16
f17
f18
f19
f20
f21
f22
f23
f24
num_lock
scroll_lock
left_shift
right_shift
left_control
right_control
left_menu
right_menu
browser_back
browser_forward
browser_refresh
browser_stop
browser_search
browser_favorites
browser_start_and_home
volume_mute
volume_Down
volume_up
next_track
previous_track
stop_media
play/pause_media
start_mail
select_media
start_application_1
start_application_2
attn_key
crsel_key
exsel_key
play_key
zoom_key
clear_key
+
,
-
.
/
`
;
[
\
]
'
`
```