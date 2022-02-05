# Some module managing nonsense
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from .models import Mode
from .forms import ShockForm, PowerConfigForm
from .shock import activate, set_power, config_state, get_power, get_mode
from time import sleep

import mechanical.presser as presser

from django.shortcuts import render

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
            set_power(mode, data['power'])
            activate(mode, data['duration'])
            locked = False
    else:
        mode = get_mode()
        form = ShockForm({'mode': int(mode),
                          'power': get_power(mode),
                          'duration': 1})
    
    context = {'form': form, 'on': presser.get_switch_state()}
    return render(request, 'collarserver/controller.html', context)

def config(request):
    
    if request.method == 'POST':
        form = PowerConfigForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            config_state(data['shock_power'], data['vibration_power'], Mode(int(data['mode'])))
    else:
        form = PowerConfigForm({
            'shock_power': get_power(Mode.SHOCK),
            'vibration_power': get_power(Mode.VIBRATION),
            'mode': get_mode()})
        
    context = {'form': form}
    return render(request, 'collarserver/config.html', context)