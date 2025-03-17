import pytest
from conftest import REG_SERVO1, REG_SERVO2, REG_UPDATE, REG_WS2812


def test_servos(smbus2_mock, pantilthat):
    pantilthat.setup()

    regs = pantilthat.pantilthat._i2c.regs

    pantilthat.servo_enable(1, True)
    pantilthat.servo_enable(2, True)

    pantilthat.servo_pulse_min(1, 510)
    pantilthat.servo_pulse_max(1, 2300)

    pantilthat.servo_pulse_min(2, 510)
    pantilthat.servo_pulse_max(2, 2300)

    pantilthat.servo_one(0)
    pantilthat.servo_two(0)

    assert regs[REG_SERVO1] == 5
    assert regs[REG_SERVO1 + 1] == 125

    assert regs[REG_SERVO2] == 5
    assert regs[REG_SERVO2 + 1] == 125


def test_servo_readback(smbus2_mock, pantilthat):
    pantilthat.setup()

    for x in range(-90, 91):
        pantilthat.pan(x)
        pantilthat.tilt(x)
        assert pantilthat.get_pan() == x, f"get_pan() should return {x}, returned {pantilthat.get_pan()}"
        assert pantilthat.get_tilt() == x, f"get_tilt() should return {x}, returned {pantilthat.get_tilt()}"


def test_servo_full_sweep(smbus2_mock, pantilthat):
    pantilthat.setup()

    for x in range(-90, 91):
        pantilthat.pan(x)
        pantilthat.tilt(x)

    for x in reversed(range(-90, 91)):
        pantilthat.pan(x)
        pantilthat.tilt(x)


def test_set_pixel(smbus2_mock, pantilthat):
    pantilthat.setup()

    regs = pantilthat.pantilthat._i2c.regs

    pantilthat.set_pixel(0, 255, 255, 255)
    pantilthat.show()

    assert sum(regs[REG_WS2812:REG_WS2812 + 72]) == 255 * 3
    assert regs[REG_UPDATE] == 1

    pantilthat.set_all(255, 255, 255)
    pantilthat.show()

    assert sum(regs[REG_WS2812:REG_WS2812 + 72]) == 255 * 3 * 24
    assert regs[REG_UPDATE] == 1


def test_servo_args(smbus2_mock, pantilthat):
    pantilthat.setup()

    # Try to enable a mythical third servo
    with pytest.raises(ValueError):
        pantilthat.servo_enable(3, True)

    with pytest.raises(ValueError):
        pantilthat.servo_enable(1, "banana")

    with pytest.raises(ValueError):
        pantilthat.servo_pulse_min(3, 510)

    with pytest.raises(ValueError):
        pantilthat.servo_pulse_max(3, 510)


def test_light_args(smbus2_mock, pantilthat):
    pantilthat.setup()

    # Try an out of range pixel
    with pytest.raises(ValueError):
        pantilthat.set_pixel(34, 255, 255, 255)

    # Try an out of range colour value
    with pytest.raises(ValueError):
        pantilthat.set_pixel(0, 256, 0, 0)


def test_brightness(smbus2_mock, pantilthat):
    pantilthat.setup()

    regs = pantilthat.pantilthat._i2c.regs

    pantilthat.brightness(222)
    assert regs[REG_WS2812] != 222

    pantilthat.light_mode(pantilthat.PWM)
    pantilthat.brightness(123)
    assert regs[REG_WS2812] == 123