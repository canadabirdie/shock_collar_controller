import RPi.GPIO as GPIO
from time import sleep

from enum import Enum, auto

class Button(Enum):
    SHOCK = auto()
    VIBRATION = auto()
    SOUND = auto()
    INCREMENT = auto()
    DECREMENT = auto()
    CHANNEL = auto()

button_to_pin = {
    Button.SHOCK: 22,
    Button.VIBRATION: 27,
    Button.SOUND: 17,
    Button.INCREMENT: 21,
    Button.DECREMENT: 20,
    Button.CHANNEL: 16
}

SWITCHPIN = 23

PAUSETIME = 0.1

GPIO.setmode(GPIO.BCM)
for pin in button_to_pin.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
GPIO.setup(SWITCHPIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def press(button, duration):
    pin = button_to_pin[button]
    GPIO.output(pin, GPIO.LOW)
    sleep(duration)
    GPIO.output(pin, GPIO.HIGH)
    # Add a quick sleep just to make sure we don't press things too fast
    sleep(PAUSETIME)

    return

def get_switch_state():
    # if the switch is flipped down, current is allowed to flow, the pin is pulled low
    return GPIO.input(SWITCHPIN)