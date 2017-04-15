from django import forms
from django.conf import settings
from datetime import date
from .models import Declaracion
from trix.widgets import TrixEditor

class DeclaracionForm(forms.ModelForm):
    fecha = forms.DateField(initial=date.today())
    class Meta:
        model = Declaracion
        exclude = []
