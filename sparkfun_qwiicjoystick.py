# The MIT License (MIT)
#
# Copyright (c) 2019 Gaston Williams
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`sparkfun_qwiicjoystick`
================================================================================

CircuitPython library for Sparkfun Qwiic Joystick


* Author(s): Gaston Williams

Implementation Notes
--------------------

**Hardware:**

*  This is library is for the SparkFun Qwiic Joystick.
*  SparkFun sells these at its website: www.sparkfun.com
*  Do you like this library? Help support SparkFun. Buy a board!
   https://www.sparkfun.com/products/15168


**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

* Adafruit's Bus Device library:
  https://github.com/adafruit/Adafruit_CircuitPython_BusDevice
"""

# imports

__version__ = "0.0.0-auto.0"
__repo__ = "https://github.com/fourstix/Sparkfun_CircuitPython_QwiicJoystick.git"

from time import sleep
from micropython import const
from adafruit_bus_device.i2c_device import I2CDevice

# public constants
QWIIC_JOYSTICK_ADDR = const(0x20) #default I2C Address

# private constants
_JOYSTICK_ID = const(0x00)
_JOYSTICK_VERSION1 = const(0x01)
_JOYSTICK_VERSION2 = const(0x02)
_JOYSTICK_X_MSB = const(0x03)
_JOYSTICK_X_LSB = const(0x04)
_JOYSTICK_Y_MSB = const(0x05)
_JOYSTICK_Y_LSB = const(0x06)
_JOYSTICK_BUTTON = const(0x07)
_JOYSTICK_STATUS = const(0x08) #1 - button clicked
_JOYSTICK_I2C_LOCK = const(0x09)
_JOYSTICK_CHANGE_ADDRESS = const(0x0A)


# class
class Sparkfun_QwiicJoystick:
    """CircuitPython class for the Sparkfun QwiicJoystick"""

    def __init__(self, i2c, address=QWIIC_JOYSTICK_ADDR, debug=False):
        """Initialize Qwiic Joystick for i2c communication."""
        self._device = I2CDevice(i2c, address)
        #save handle to i2c bus in case address is changed
        self._i2c = i2c
        self._debug = debug

# public properites

    @property
    def connected(self):
        """Check the id of Joystick.  Returns True if successful."""
        if self._read_register(_JOYSTICK_ID) != QWIIC_JOYSTICK_ADDR:
            return False
        return True

    @property
    def version(self):
        """Return the version string for the Joystick firmware."""
        major = self._read_register(_JOYSTICK_VERSION1)
        minor = self._read_register(_JOYSTICK_VERSION2)
        return 'v' + str(major) + '.' + str(minor)

    @property
    def horizontal(self):
        """Return the X value 0 - 1023 of the joystick postion."""
        # Read MSB for horizontal joystick position
        x_msb = self._read_register(_JOYSTICK_X_MSB)
        # Read LSB for horizontal joystick position
        x_lsb = self._read_register(_JOYSTICK_X_LSB)

        # mask off bytes and combine into 10-bit integer
        x = ((x_msb & 0xFF)<<8 | (x_lsb & 0xFF))>>6
        return x

    @property
    def vertical(self):
        """Return the Y value 0 to 1023 of the joystick postion."""
        # Read MSB for veritical joystick position
        y_msb = self._read_register(_JOYSTICK_Y_MSB)
        # Read LSB for vertical joystick position
        y_lsb = self._read_register(_JOYSTICK_Y_LSB)

        # mask off bytes and combine into 10-bit integer
        y = ((y_msb & 0xFF)<<8 | (y_lsb & 0xFF))>>6
        return y

    @property
    def button(self):
        """Return 0 if button is down, 1 if up."""
        button = self._read_register(_JOYSTICK_BUTTON)
        return button

    # Issue: register 0x08 always contains 1 for some reason, even when cleared
    @property
    def button_status(self):
        """Return 1 if button pressed between reads. Button status is cleared."""
        #read button status (since last check)
        status = self._read_register(_JOYSTICK_STATUS)
        #clear button status
        self._write_register(_JOYSTICK_STATUS, 0x00)
        return status & 0xFF


# public functions

    def set_i2c_address(self, new_address):
        """Change the i2c address of Joystick snd return True if successful."""
        # check range of new address
        if (new_address < 8 or new_address > 119):
            print('ERROR: Address outside 8-119 range')
            return False
        # write magic number 0x13 to lock register, to unlock address for update
        self._write_register(_JOYSTICK_I2C_LOCK, 0x13)
        # write new address
        self._write_register(_JOYSTICK_CHANGE_ADDRESS, new_address)

	# wait a second for joystick to settle after change
        sleep(1)

        # try to re-create new i2c device at new address
        try:
            self._device = I2CDevice(self._i2c, new_address)
        except ValueError as err:
            print('Address Change Failure')
            print(err)
            return False

        #if we made it here, everything went fine
        return True

# No i2c begin function is needed since I2Cdevice class takes care of that

# private functions

    def _read_register(self, addr):
        # Read and return a byte from the specified 8-bit register address.
        with self._device as device:
            device.write(bytes([addr & 0xFF]), stop=False)
            result = bytearray(1)
            device.readinto(result)
            if self._debug:
                print("$%02X => %s" % (addr, [hex(i) for i in result]))
            return result[0]

    def _write_register(self, addr, value):
        # Write a byte to the specified 8-bit register address
        with self._device as device:
            device.write(bytes([addr & 0xFF, value & 0xFF]))
            if self._debug:
                print("$%02X <= 0x%02X" % (addr, value))
