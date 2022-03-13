# Display, request handling and authentication

# Some module managing nonsense
from pathlib import Path
import sys

from django.http import HttpResponse
path_root = Path(__file__).parents[2]
sys.path.append(str(path_root))

from time import sleep

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from rest_framework.parsers import JSONParser

from .forms import ShockForm
from .shock import activate
from .models import Function, string_to_func

from mechanical import presser

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

def api_shock(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(username = data["username"], password = data["password"])
        if user is None:
            response = HttpResponse("")
            response.status_code = 400
            return response
        else:
            mode = string_to_func[data["function"]]
            global locked
            while locked:
                sleep(1)
            locked = True
            activate(mode, data['duration'], data['power'])
            locked = False
            response = HttpResponse("")
            response.status_code = 200
            return response