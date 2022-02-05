from django.db import models
from enum import IntEnum, auto

MINPOWER = 0
MAXPOWER = 99

class Mode(IntEnum):
    SHOCK = auto()
    VIBRATION = auto()
    SOUND = auto()

class ControllerState(models.Model):
    last_press_time = models.FloatField(default=0)
    mode = models.IntegerField(default=Mode.SHOCK)
    vibration_power = models.IntegerField(default=0)
    shock_power = models.IntegerField(default=0)