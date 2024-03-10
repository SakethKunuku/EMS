from django import forms
from .models import *

class EventApplicationForm(forms.ModelForm):
    class Meta:
        model = EventApplication
        fields = ['name','email','resume','cover_letter']
    def __init__(self, *args, **kwargs):
        super(EventApplicationForm, self).__init__(*args, **kwargs)