from conftest import REG_CONFIG


def test_setup(smbus2_mock, pantilthat):
    pantilthat.setup()


def test_consts(smbus2_mock, pantilthat):
    assert pantilthat.WS2812 == 1, "pantilthat.WS2812 should equal 1"
    assert pantilthat.PWM == 0, "pantilthat.PWM should equal 0"
    assert pantilthat.RGB == 0, "pantilthat.RGB should equal 0"
    assert pantilthat.GRB == 1, "pantilthat.GRB should equal 1"
    assert pantilthat.RGBW == 2, "pantilthat.RGBW should equal 2"
    assert pantilthat.GRBW == 3, "pantilthat.GRBW should equal 3"


def test_default_config(smbus2_mock, pantilthat):
    pantilthat.setup()

    regs = pantilthat.pantilthat._i2c.regs

    assert regs[REG_CONFIG] == 0b00001100, f"Config reg incorrect!: {regs[REG_CONFIG]}"