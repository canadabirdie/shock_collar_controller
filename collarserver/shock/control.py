# Display, request handling and authentication

# Some module managing nonsense
from pathlib import Path
import sys
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from mechanical import presser
from time import sleep

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ShockForm
from .shock import activate
from .models import Function

locked = False

@login_required
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
        form = ShockForm({'mode': int(Function.SHOCK),
                          'power': 0,
                          'duration': 1})
    
    context = {'form': form, 'on': presser.get_switch_state()}
    return render(request, 'collarserver/controller.html', context)