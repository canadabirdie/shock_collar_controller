from django.db import models
from enum import IntEnum
from django.core.validators import MaxValueValidator, MinValueValidator

MINPOWER = 0
MAXPOWER = 99
    
class Function(IntEnum):
    SHOCK = 1
    VIBRATE = 2
    SOUND = 3

string_to_func = {"shock": Function.SHOCK, "vibrate": Function.VIBRATE, "sound": Function.SOUND}

int_to_func = {1: Function.SHOCK, 2: Function.VIBRATE, 3: Function.SOUND}
func_to_int = {Function.SHOCK: 1, Function.VIBRATE: 2, Function.SOUND: 3}
