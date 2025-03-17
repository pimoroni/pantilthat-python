import sys

import mock
import pytest

REG_CONFIG = 0x00
REG_SERVO1 = 0x01
REG_SERVO2 = 0x03
REG_WS2812 = 0x05
REG_UPDATE = 0x4e


class SMBus:
    def __init__(self, bus_id):
        self.regs = [0 for _ in range(79)]

        self.regs[REG_CONFIG] = 0
        self.regs[REG_SERVO1] = 0
        self.regs[REG_SERVO1 + 1] = 0
        self.regs[REG_SERVO2] = 0
        self.regs[REG_SERVO2 + 1] = 0
        self.regs[REG_WS2812] = 0
        self.regs[REG_UPDATE] = 0

    def write_i2c_block_data(self, addr, reg, data):
        for index, value in enumerate(data):
            self.regs[reg + index] = value

    def write_word_data(self, addr, reg, data):
        self.regs[reg] = (data >> 8) & 0xff
        self.regs[reg + 1] = data & 0xff

    def write_byte_data(self, addr, reg, data):
        self.regs[reg] = data & 0xff

    def read_byte_data(self, addr, reg):
        return self.regs[reg]

    def read_word_data(self, addr, reg):
        return (self.regs[reg] << 8) | self.regs[reg + 1]


@pytest.fixture(scope="function", autouse=False)
def smbus2_mock():
    smbus = mock.Mock()
    smbus.SMBus = SMBus
    sys.modules["smbus2"] = smbus
    yield smbus
    del sys.modules["smbus2"]


@pytest.fixture(scope="function", autouse=False)
def pantilthat():
    import pantilthat
    yield pantilthat
    del sys.modules["pantilthat"]
