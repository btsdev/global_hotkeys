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

# Bindings take on the form of <binding>, on_press_callback, on_release_callback, actuate_on_partial_release_flag
# It's useful to have 'actuate_on_partial_release_flag' set to False, so your modifier keys don't get in the way of any automatic keyboard output you're doing in response.

# Note the actual hotkey syntax. Key combinations are denoted via the '+' character, and additional key chords are separated by commas. Spaces are ignored.

# Register all of our keybindings
register_hotkeys(bindings)

# Finally, start listening for keypresses
start_checking_hotkeys()

# Keep waiting until the user presses the exit_application keybinding.
# Note that the hotkey listener will exit when the main thread does.
while is_alive:
    time.sleep(0.1)
```

## Also note that I've included a simple global snippets example using this functionality.
It's in the `tests` folder if you download this project's source from [GitHub](https://github.com/btsdev/global_hotkeys).

It's the file `global_snippets.py` and it demonstrates toggling on and off global snippets using a hotkey, and using key chords to inject snippets, in this case the current date time. This is a nod to a user who emailed regarding the addition of this functionality.

It achieves this by pasting in the current date time to any input field after backspacing to erase the snippet's chord from the input field (careful where you use it though. For faster input of snippets, I relied on just placing the date string into the clipboard and emulating CTRL+V to paste).

Also, it uses the winsound library's Beep function to emit a low and subtle visual cue to indicate whether you just toggled the global snippets on or off.

`I personally use the Hyperkey (which is basically Window+Control+Shift+Alt) to avoid clashing with most application's own hotkeys, which is normally not available in windows, but it can be setup using [Autohotkey](https://stackoverflow.com/questions/40435980/how-to-emulate-hyper-key-in-windows-10-using-autohotkey) and also applying the [OfficeKeyFix](https://github.com/anthonyheddings/OfficeKeyFix) which you'll need to compile yourself if one is interested. I personally mapped it to my right control key instead of the capslock key; it was just a simple edit to the Autohotkey script. Both of these I placed in my windows startup folder, and then I was all set.`

## Additional functionality

You may also add/remove keybindings one at a time, in bulk, or completely clear them all out (which also stops the hotkey listener thread).

```python

# Just reusing our bindings declaration from above (this is not a complete code example, btw).
bindings = [
    ["control + 7, control + 4", None, print_world, True],
    ["control + 5", None, print_hello, False],
    ["window + 1", None, print_foo, False],
    ["t,m", None, print_bar, False],
    ["control + Q", None, exit_application, False],
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
left_window
right_window
window
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