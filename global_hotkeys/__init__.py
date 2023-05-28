from .hotkey_checker import hotkey_checker

def _syntax_check(binding):
    if(isinstance(binding, list)):
        hotkey_string = str(binding)
        valid_hotkey_string = " + ".join(binding)
        raise Exception(
            "You've specified the hotkey as a list. The syntax has changed to being specified as a string now.\n"+
            f"Your hotkey {hotkey_string} should now be specified as \"{valid_hotkey_string}\""
        )

def register_hotkey(binding, press_callback, release_callback, actuate_on_partial_release):
    _syntax_check(binding)
    return hotkey_checker.register_hotkey([hotkey.split("+") for hotkey in binding.replace(" ","").split(",")], press_callback, release_callback, actuate_on_partial_release)

def _register_hotkey(binding, press_callback, release_callback, actuate_on_partial_release):
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
        _syntax_check(_binding)
        binding = [hotkey.split("+") for hotkey in _binding.replace(" ","").split(",")]
        _register_hotkey(binding, keydown_function, keyup_function, actuate_on_partial_release)

def remove_hotkeys(bindings):
    for _binding in bindings:
        binding = [hotkey.split("+") for hotkey in _binding.replace(" ","").split(",")]
        remove_hotkey(binding)

# Remove all keybindings.
# *Note that this also stops the hotkey checking thread.
def clear_hotkeys():
    hotkey_checker.clear_bindings()