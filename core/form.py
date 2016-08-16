from django.forms import ModelForm
from .models import Aval


class AvalprofForm(ModelForm):
    class Meta:
        model = Avalprof
        exclude = ['']
