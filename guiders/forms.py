from django import forms
from .models import Guider

class GuiderForm(forms.ModelForm):
    class Meta:
        model = Guider
        fields = ['name', 'age', 'service_hours']
