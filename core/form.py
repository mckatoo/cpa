from django.forms import ModelForm
from .models import Avalprof


class AvalprofForm(ModelForm):
    class Meta:
        model = Avalprof
        exclude = ['']
