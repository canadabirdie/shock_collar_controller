# Some module managing nonsense
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from time import time, sleep

import mechanical.presser as presser
from mechanical.presser import Button
from .models import ControllerState, MINPOWER, MAXPOWER, Mode

PRESS_TIME = 0.1

mode_to_button = {
    Mode.SHOCK: Button.SHOCK,
    Mode.VIBRATION: Button.VIBRATION,
    Mode.SOUND: Button.SOUND
}

if len(ControllerState.objects.all()) == 0:
    c = ControllerState(last_press_time = 0, power_level = 0)
    c.save()
else:
    c = ControllerState.objects.last()
    
def activate(mode, duration):
    _check_for_sleep()
    press(mode_to_button[mode], duration)
    global c
    c.mode = mode
    c.save()
    return

def set_power(mode, power):
    if mode == Mode.SOUND:
        return
    if mode != c.mode:
        activate(mode, PRESS_TIME)
    if abs(power - get_power(mode)) > 50: # Check if it's faster to wrap around
        # Then bring it up or down until it wraps around. Just get it to maxpower or minpower
        # The while loops after this will do the rest of the work
        if power > get_power(mode):
            while get_power(mode) != MAXPOWER: 
                _decrement_power(mode)
        else:  # Target power is less than current power. Need to go up
            while get_power(mode) != MINPOWER:
                _increment_power(mode)
    while get_power(mode) < power:
        _increment_power(mode)
    while get_power(mode) > power:
        _decrement_power(mode)
    
def _check_for_sleep():
    time_delta = time()-c.last_press_time
    # Sleep happens after 30 seconds. To be safe, if it's been at least 25 seconds, wait until
    # it's been at least 35 seconds before pressing the button
    if time_delta > 25:
        if time_delta < 35:
            sleep(35-time_delta)
        press(Button.INCREMENT, PRESS_TIME)
        
    
def _increment_power(mode):
    global c
    if mode != c.mode:
        activate(mode, PRESS_TIME)
    _check_for_sleep()
    press(Button.INCREMENT, PRESS_TIME)
    if mode == Mode.SHOCK:
        c.shock_power += 1
        if c.shock_power == MAXPOWER+1:
            c.shock_power = MINPOWER
    elif mode == Mode.VIBRATION:
        c.vibration_power += 1
        if c.vibration_power == MAXPOWER+1:
            c.vibration_power = MINPOWER
    else:
        raise ValueError
    c.save()

def _decrement_power(mode):
    global c
    if mode != c.mode:
        activate(mode, PRESS_TIME)
    _check_for_sleep()
    press(Button.DECREMENT, PRESS_TIME)
    if mode == Mode.SHOCK:
        c.shock_power -= 1
        if c.shock_power == MINPOWER-1:
            c.shock_power = MAXPOWER
    elif mode == Mode.VIBRATION:
        c.vibration_power -= 1
        if c.vibration_power == MINPOWER-1:
            c.vibration_power = MAXPOWER
    else:
        raise ValueError
    c.save()
    
def press(button, duration):
    global c
    presser.press(button, duration)
    c.last_press_time = time()
    c.save()
    
def config_state(shock_power, vibration_power, mode):
    global c
    c.shock_power = shock_power
    c.vibration_power = vibration_power
    c.mode = mode
    c.save()
    
def get_power(mode):
    if mode == Mode.SHOCK:
        return c.shock_power
    elif mode == Mode.VIBRATION:
        return c.vibration_power
    elif mode == Mode.SOUND:
        return 0
    raise ValueError
    
def get_mode():
    return c.mode