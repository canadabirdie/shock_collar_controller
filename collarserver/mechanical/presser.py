import RPi.GPIO as GPIO
from time import sleep
import serial
from time import time, sleep
import typing

from enum import Enum, auto

SWITCHPIN = 23

GPIO.setmode(GPIO.BCM)
GPIO.setup(SWITCHPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# May differ depending on your device and things. After you've plugged in your arduino,
# the command dmesg | grep "tty" should help. Look at the last few lines, should be something
# like
# [1036084.518057] cdc_acm 1-1.4:1.0: ttyACM0: USB ACM device
ser = serial.Serial('/dev/ttyACM0', 9600, timeout = 1)
ser.reset_input_buffer()

def send(bits: str, duration: int):
    end_time = time() + duration
    while time() < end_time:
        ser.write(bytes(bits, 'ascii'))
        sleep(0.1)
    return

def get_switch_state():
    # if the switch is flipped down, current is allowed to flow, the pin is pulled low
    return GPIO.input(SWITCHPIN)