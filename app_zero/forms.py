from django import forms
from .models import ZeroModel

class ZeroSubmitForm:

    left = forms.DecimalField()
    right = forms.DecimalField()
    step = forms.DecimalField()
    frequency = forms.DecimalField()