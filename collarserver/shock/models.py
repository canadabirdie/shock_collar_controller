from django.db import models
from enum import IntEnum

MINPOWER = 0
MAXPOWER = 99
    
class Function(IntEnum):
    SHOCK = 1
    VIBRATE = 2
    SOUND = 3