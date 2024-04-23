# Python Global Hotkey Bindings for Windows

Use this library to set system wide keybindings for your code to respond to.

## Installation

```
pip install global-hotkeys -U
```

## Example usage

```python
from global_hotkeys import *

import time

# Flag to indicate whether the program should continue running.
is_alive = True

def print_hello():
    print("Hello")

def print_world():
    print("World")

def print_foo():
    print("Foo")

def print_bar():
    print("Bar")

def print_with_params(params):
    print(params["test"])

def press_with_params(params):
    print(params["press_param"])

def release_with_params(params):
    print(params["release_param"])

def exit_application():
    global is_alive
    print("exiting")
    stop_checking_hotkeys()
    is_alive = False


# Declare some key bindings.
bindings = [
    ["control + 7, control + 4", None, print_world, True],
    # You can use direct keycodes as well (useful for non-US keyboard layouts):
    ["control + 0x35", None, print_hello, False], # 0x35 is the keycode for the '5' key
    ["control + 6", None, print_with_params, False, {"test":5}],
    [
        "control + 8", 
        press_with_params, 
        release_with_params, 
        False, 
        {"press_param":"pressed!"}, 
        {"release_param": "released!"}
    ],
    # dict style
    {
        "hotkey": "control + 4",
        "on_press_callback": None,
        "on_release_callback": print_with_params,
        "actuate_on_partial_release": False,
        "callback_params": {"test": "testing"},

    },
    # dict style with differentiating params for press and release callbacks
    {
        "hotkey": "control + 9",
        "on_press_callback": press_with_params,
        "on_release_callback": release_with_params,
        "actuate_on_partial_release": False,
        "press_callback_params": {"press_param":"ctrl+9 pressed!"},
        "release_callback_params": {"release_param": "ctrl+9 released!"},

    },

    ["window + 1", None, print_foo, False],
    ["t,m", None, print_bar, False],
    ["control + Q", None, exit_application, False],
]

# Bindings take on the form of:
#   <binding>, on_press_callback, on_release_callback, actuate_on_partial_release_flag, callback_params
#
# *Note that callback_params will be passed to both press and release callback functions
#
# Or in explicit dict format:
# {
#     "hotkey": <binding>,
#     "on_press_callback": <press_callback>,
#     "on_release_callback": <release_callback>,
#     "actuate_on_partial_release": False | True,
#     "callback_params": <a variable or expression can go here>  <-- This applies to both callbacks.
#     "press_callback_params": <a variable or expression can go here>
#     "release_callback_params": <a variable or expression can go here>
# }

# It's useful to have 'actuate_on_partial_release_flag' set to False, 
# so your modifier keys don't get in the way of any automatic keyboard output you're doing in response.

# Note the actual hotkey syntax. Key combinations are denoted via the '+' character, 
# and additional key chords are separated by commas. Spaces are ignored.

# Register all of our keybindings
register_hotkeys(bindings)

# Finally, start listening for keypresses
start_checking_hotkeys()

# Keep waiting until the user presses the exit_application keybinding.
# Note that the hotkey listener will exit when the main thread does.
while is_alive:
    time.sleep(0.1)
```

## Explanation of the binding structure

Let's go in more details on how the binding is structured, You have two options either to declare the binding explicitly like this within curly brackets:
```
# {
#     "hotkey": <binding>,
#     "on_press_callback": <press_callback>,
#     "on_release_callback": <release_callback>,
#     "actuate_on_partial_release": False | True,
#     "callback_params": 1ms": <a variable or expression can go here>
#     "release_callback_params": <a variable or expression can go here>
# }
```

Or implicitly by the position of the parameter:
```
["hotkey", on_press_callback, on_release_callback, actuate_on_partial_release,press_callback_params,release_callback_params]
```
- **hotkey:** A string representing the key combination that triggers the callbacks, such as "control + 7, control + 4".
- **on_press_callback:** The function to be called when the hotkey is pressed. Can be None or a function reference.
- **on_release_callback:** The function to be called when the hotkey is released. Can be None or a function reference.
- **actuate_on_partial_release:** A boolean indicating whether the release callback should be triggered on a partial release of the key combination.
- **callback_params:** Parameters to be passed to both the press and release callbacks. This should be a dictionary.
- **press_callback_params, release_callback_params:** Parameters specifically for the press,release callbacks. This should be a dictionary (key-value pairs Like in this example ```"press_callback_params": {"press_param":"ctrl+9 pressed!"}```) .

## If you are on a non-US keyboard layout...
You may need to manually figure out the keycodes for the keys you want to bind to, and use those keycodes directly instead of the keynames in your bindings. I've included a useful utility for doing so. 

Just open an interactive shell, and import my keycode_checker module to begin figuring out what your desired keys' keycodes are.
```python
>>> from global_hotkeys import keycode_checker
```
You'll see the `Press any key (Ctrl+C to exit)` prompt and can begin pressing keys until you've gathered your desired keycodes:
```
Key pressed: a
VK Code: 0x1E
Key pressed: b
VK Code: 0x30
```

And in your code that's actually setting up keybindings maybe you'd use something like:
```python
# Assume our previous example setup code from above
bindings = [
    ["control + 0x1E", None, print_hello, False],
    # whatever other bindings...
]
```

That said, if your modifier keys' keycodes (e.g. for control, shift, alt) are different than what's listed in [keycodes.py](https://github.com/btsdev/global_hotkeys/blob/master/global_hotkeys/keycodes.py), you'll likely need to just fork this project and modify the source to make things work. CD into your forked copy of the repos and use `pip install -e ./` to apply your changes as you experiment and use your forked version of the library instead. Certainly not a perfect solution, admittedly...

As the code needs to differentiate between modifier keys and non-modifier keys, some further update may be necessary to allow for changing/specifying modifier keycodes as well for non-US keyboard layouts.

## Also note that I've included a simple global snippets example using this functionality.
It's in the `tests` folder if you download this project's source from [GitHub](https://github.com/btsdev/global_hotkeys).

It's the file `global_snippets.py` and it demonstrates toggling on and off global snippets using a hotkey, and using key chords to inject snippets, in this case the current date time. This is a nod to a user who emailed regarding the addition of this functionality.

It achieves this by pasting in the current date time to any input field after backspacing to erase the snippet's chord from the input field (careful where you use it though. For faster input of snippets, I relied on just placing the date string into the clipboard and emulating CTRL+V to paste).

Also, it uses the winsound library's Beep function to emit a low and subtle visual cue to indicate whether you just toggled the global snippets on or off.

### Try setting up and using the Hyperkey to avoid hotkey conflicts with your applications.
I personally use the Hyperkey (which is basically Window+Control+Shift+Alt and also known as the 'OfficeKey' on keyboards that have actually have it) to avoid clashing with most applications' own hotkeys, which is normally not available in windows, but it can be setup using [Autohotkey](https://stackoverflow.com/questions/40435980/how-to-emulate-hyper-key-in-windows-10-using-autohotkey) and also applying the [OfficeKeyFix](https://github.com/anthonyheddings/OfficeKeyFix) which you'll need to compile yourself if one is interested. You can read more about the officekey issue on [Super User](https://superuser.com/questions/1455857/how-to-disable-office-key-keyboard-shortcut-opening-office-app). I personally mapped it to my right control key instead of the capslock key; it was just a simple edit to the Autohotkey script. Both of these I placed in my windows startup folder, and then I was all set.

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

# Register a single keybinding (if it's not already registered). 
# Returns True if the key didn't already exist and was added, 
# else False (the binding is already registered - remove it first if 
# you wish to overwrite it with new event handlers).
register_hotkey(bindings[0])

# Remove a single keybinding (if it exists). 
# Returns True if the key existed and was removed, else False (the binding is already gone).
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
space
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
enter
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
