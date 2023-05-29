from .hotkey_checker import hotkey_checker

def _syntax_check(binding):
    if(isinstance(binding, list)):
        hotkey_string = str(binding)
        valid_hotkey_string = " + ".join(binding)
        raise Exception(
            "You've specified the hotkey as a list. The syntax has changed to being specified as a string now.\n"+
            f"Your hotkey {hotkey_string} should now be specified as \"{valid_hotkey_string}\""
        )

def retrofit_old_bindings(binding):
     if isinstance(binding, list):
          return " + ".join(binding)
     return binding

def sanitize_binding(binding_raw):
    if (isinstance(binding_raw, list)):
        _binding = retrofit_old_bindings(binding_raw[0])
        keydown_function = binding_raw[1]
        keyup_function = binding_raw[2]
        actuate_on_partial_release = True
        if len(binding_raw) > 3:
            actuate_on_partial_release = binding_raw[3]
        params = None
        if len(binding_raw) > 4:
            params = binding_raw[4]
        return [_binding, keydown_function, keyup_function, actuate_on_partial_release, params]
    elif (isinstance(binding_raw, dict)):
        _binding = retrofit_old_bindings(binding_raw["hotkey"])
        keydown_function = binding_raw["on_press_callback"]
        keyup_function = binding_raw["on_release_callback"]
        actuate_on_partial_release = True
        if "actuate_on_partial_release" in binding_raw:
            actuate_on_partial_release = binding_raw["actuate_on_partial_release"]
        params = None
        if "callback_params" in binding_raw:
            params = binding_raw["callback_params"]
        return [_binding, keydown_function, keyup_function, actuate_on_partial_release, params]
    else:
        binding_raw_str = str(binding_raw)
        raise Exception(f"Binding {binding_raw_str} is not the correct_type")

def register_hotkey(binding, press_callback, release_callback, actuate_on_partial_release = False, params = None):
    _syntax_check(binding)
    return hotkey_checker.register_hotkey([hotkey.split("+") for hotkey in binding.replace(" ","").split(",")], press_callback, release_callback, actuate_on_partial_release, params)
 
def _register_hotkey(binding, press_callback, release_callback, actuate_on_partial_release, params):
	return hotkey_checker.register_hotkey(binding, press_callback, release_callback, actuate_on_partial_release, params)

def remove_hotkey(binding):
	return hotkey_checker.remove_hotkey(binding)

def start_checking_hotkeys():
	hotkey_checker.start_checking_hotkeys()

def stop_checking_hotkeys():
	hotkey_checker.shutdown_checker()

def restart_checking_hotkeys():
	hotkey_checker.restart_checker()

def register_hotkeys(bindings):
    for binding_raw in bindings:
        _binding, keydown_function, keyup_function, actuate_on_partial_release, params = sanitize_binding(binding_raw)
        _syntax_check(_binding)
        binding = [hotkey.split("+") for hotkey in _binding.replace(" ","").split(",")]
        _register_hotkey(binding, keydown_function, keyup_function, actuate_on_partial_release, params)

def remove_hotkeys(bindings):
    for _binding in bindings:
        binding = [hotkey.split("+") for hotkey in _binding.replace(" ","").split(",")]
        remove_hotkey(binding)

# Remove all keybindings.
# *Note that this also stops the hotkey checking thread.
def clear_hotkeys():
    hotkey_checker.clear_bindings()