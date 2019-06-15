#  This is example is for the SparkFun Qwiic Joystick.
#  SparkFun sells these at its website: www.sparkfun.com
#  Do you like this library? Help support SparkFun. Buy a board!
#  https://www.sparkfun.com/products/15168

"""
 Qwiic Joystick Simple Test - qwiicjoystick_simpletest.py
 Written by Gaston Williams, June 13th, 2019
 The Qwiic Joystick is a I2C controlled analog joystick

 Simple Test:
 This program uses the Qwiic Joystick CircuitPython Library to read
 and print out the joystick position.
"""

from time import sleep
import board
import busio
import sparkfun_qwiicjoystick

# Create bus object using our board's I2C port
i2c = busio.I2C(board.SCL, board.SDA)

# Create joystick object
joystick = sparkfun_qwiicjoystick.Sparkfun_QwiicJoystick(i2c)

# Check if connected
if joystick.connected:
    print('Joystick connected.')
else:
    print('Joystick does not appear to be connected. Please check wiring.')
    exit()

print('Press Joystick button to exit program.')

while joystick.button == 1:
    print('X = ' + str(joystick.horizontal) + ' Y = ' + str(joystick.vertical))
    sleep(0.200)  # sleep a bit to slow down messages

print('Button pressed.')
