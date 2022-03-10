from .shock import MINPOWER, MAXPOWER
from django import forms
from .models import Function

mode_choices = (
    (int(Function.SHOCK), "Shock"),
    (int(Function.VIBRATE), "Vibrate"),
    (int(Function.SOUND), "Sound")
)

class ShockForm(forms.Form):
    duration = forms.FloatField(label='Duration', min_value=0, max_value=10, initial=1)
    power = forms.IntegerField(label='Power', min_value=MINPOWER, max_value=MAXPOWER, initial=0)
    mode = forms.ChoiceField(choices=mode_choices, initial=Function.SHOCK)
    
class PowerConfigForm(forms.Form):
    shock_power = forms.IntegerField(label='Shock power', min_value=MINPOWER, max_value=MAXPOWER)
    vibration_power = forms.IntegerField(label='Vibration power', min_value=MINPOWER, max_value=MAXPOWER)
    mode = forms.ChoiceField(choices=mode_choices)