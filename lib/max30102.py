# pylint: disable=import-error
from micropython import const

from adafruit import i2c_device

_MAX30102_I2C_WRITE_ADDR = const(0xAE)
_MAX30102_I2C_READ_ADDR = const(0xAF)

#register addresses
_MAX30102_REG_INTR_STATUS_1 = const(0x00)
_MAX30102_REG_INTR_STATUS_2 = const(0x01)
_MAX30102_REG_INTR_ENABLE_1 = const(0x02)
_MAX30102_REG_INTR_ENABLE_2 = const(0x03)
_MAX30102_REG_FIFO_WR_PTR = const(0x04)
_MAX30102_REG_OVF_COUNTER = const(0x05)
_MAX30102_REG_FIFO_RD_PTR = const(0x06)
_MAX30102_REG_FIFO_DATA = const(0x07)
_MAX30102_REG_FIFO_CONFIG = const(0x08)
_MAX30102_REG_MODE_CONFIG = const(0x09)
_MAX30102_REG_SPO2_CONFIG = const(0x0A)
_MAX30102_REG_LED1_PA = const(0x0C)
_MAX30102_REG_LED2_PA = const(0x0D)
_MAX30102_REG_PILOT_PA = const(0x10)
_MAX30102_REG_MULTI_LED_CTRL1 = const(0x11)
_MAX30102_REG_MULTI_LED_CTRL2 = const(0x12)
_MAX30102_REG_TEMP_INTR = const(0x1F)
_MAX30102_REG_TEMP_FRAC = const(0x20)
_MAX30102_REG_TEMP_CONFIG = const(0x21)
_MAX30102_REG_PROX_INT_THRESH = const(0x30)
_MAX30102_REG_REV_ID = const(0xFE)
_MAX30102_REG_PART_ID = const(0xFF)

class Max30102():

    def __init__(self, i2c, address=_):
        self._device  = i2c_device.I2CDevice(i2c)
        
        try:
            self.write(_MAX30102_REG_INTR_ENABLE_1, 0xC0)
            self.write(_MAX30102_REG_INTR_ENABLE_2, 0x00)
            self.write(_MAX30102_REG_FIFO_WR_PTR, 0x00)
            self.write(_MAX30102_REG_OVF_COUNTER, 0x00)
            self.write(_MAX30102_REG_FIFO_RD_PTR, 0x00)
            self.write(_MAX30102_REG_FIFO_CONFIG, 0x4F)
            self.write(_MAX30102_REG_MODE_CONFIG, 0x03)
            self.write(_MAX30102_REG_SPO2_CONFIG, 0x27)
            self.write(_MAX30102_REG_LED1_PA, 0x24)
            self.write(_MAX30102_REG_LED2_PA, 0x24)
            self.write(_MAX30102_REG_PILOT_PA, 0x7F)
        except:
            

    _BUFFER = bytearray(2)
    def write(self, addr, data):
        with self._device as i2c:
            self._BUFFER[0] = addr & 0xFF
            self._BUFFER[1] = val & 0xFF
            i2c.write(self._BUFFER, end=2)

    def read(self, addr, buf):
        with self._device as i2c:
            i2c.write_then_readinto(bytes([addr & 0xFF], buf, in_end=1))

    