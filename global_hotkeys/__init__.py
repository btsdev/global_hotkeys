from .hotkey_checker import hotkey_checker

def register_hotkey(binding, press_callback, release_callback, actuate_on_partial_release):
	return hotkey_checker.register_hotkey(binding, press_callback, release_callback, actuate_on_partial_release)

def remove_hotkey(binding):
	return hotkey_checker.remove_hotkey(binding)

def start_checking_hotkeys():
	hotkey_checker.start_checking_hotkeys()

def stop_checking_hotkeys():
	hotkey_checker.shutdown_checker()

def restart_checking_hotkeys():
	hotkey_checker.restart_checker()

def register_hotkeys(bindings):
    for _binding, keydown_function, keyup_function, actuate_on_partial_release in bindings:
        binding = [hotkey.split("+") for hotkey in _binding.replace(" ","").split(",")]
        register_hotkey(binding, keydown_function, keyup_function, actuate_on_partial_release)

def remove_hotkeys(bindings):
    for _binding in bindings:
        binding = [hotkey.split("+") for hotkey in _binding.replace(" ","").split(",")]
        remove_hotkey(binding)

# Remove all keybindings.
# *Note that this also stops the hotkey checking thread.
def clear_hotkeys():
    hotkey_checker.clear_bindings()