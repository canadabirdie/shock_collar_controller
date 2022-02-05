# Some module managing nonsense
from bisect import bisect
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

import typing

from time import time, sleep

from mechanical import presser
from .models import MINPOWER, MAXPOWER, Function

func_to_string = {Function.SHOCK: '01', Function.VIBRATE: '10', Function.SOUND: '11'}

def bits_with_padding(value: int, padding: int) -> str:
    return format(value, f'0{padding}b')

WORDLEN = 8

def checksum(message: str) -> str:
    chunks = [message[i:i+WORDLEN] for i in range(0, len(message), WORDLEN)]
    return format(sum(int(x, 2) for x in chunks), f'0{WORDLEN}b')

# Given a channel, intensity and message type, returns the bitstring to produce that behavior. Also, channels start counting from 0
def get_bits(channel: int, function: Function, intensity: int) -> str:
    # The meat of the message.
    meat = f"010110000001010000{bits_with_padding(channel, 2)}00{func_to_string[function]}{bits_with_padding(intensity, 8)}"
    # Add the checksum and leading/trailing bits, not including first or last 0 bits
    return meat+checksum(meat)+"00"
    
def activate(mode: Function, duration: int, power: int):
    # Get the bit representation
    bits = get_bits(0, mode, power)
    presser.send(bits, duration)
    return