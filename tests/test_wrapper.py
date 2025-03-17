def test_wrapped_functions(smbus2_mock, pantilthat):
    for method in ["idle_timeout", "servo_enable", "servo_pulse_max", "servo_pulse_min",
               "brightness", "clear", "light_mode", "light_type", "set_all",
               "set_pixel", "set_pixel_rgbw", "show",
               "servo_one", "pan", "get_pan", "get_servo_one",
               "servo_two", "tilt", "get_tilt", "get_servo_two"]:
        assert hasattr(pantilthat, method), "Method {method}() should exist!".format(method=method)
        assert callable(getattr(pantilthat, method)), "Method {method}() should be callable!".format(method=method)

def test_function_alises(smbus2_mock, pantilthat):
    assert pantilthat.pan == pantilthat.servo_one, "Method 'pan' should alias 'servo_one'"
    assert pantilthat.tilt == pantilthat.servo_two, "Method 'tilt' should alias 'servo_two'"
    assert pantilthat.get_pan == pantilthat.get_servo_one, "Method 'get_pan' should alias 'get_servo_one'"
    assert pantilthat.get_tilt == pantilthat.get_servo_two, "Method 'get_tilt' should alias 'get_servo_two'"
