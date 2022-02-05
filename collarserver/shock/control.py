# Some module managing nonsense
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from mechanical import presser
from time import sleep
from enum import Enum

from django.shortcuts import render

from .forms import ShockForm
from .shock import activate

class Function(Enum):
    SHOCK = 1
    VIBRATE = 2
    SOUND = 3

locked = False

def controller(request):
    
    if request.method == 'POST':
        form = ShockForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            mode = int(data['mode'])
            global locked
            while locked:
                sleep(1)
            locked = True
            activate(mode, data['duration'], data['power'])
            locked = False
    else:
        form = ShockForm({'mode': Function.SHOCK,
                          'power': 0,
                          'duration': 1})
    
    context = {'form': form, 'on': presser.get_switch_state()}
    return render(request, 'collarserver/controller.html', context)