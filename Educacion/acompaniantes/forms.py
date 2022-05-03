from django import forms
from .models import Acompaniante

class AcompanianteForm(forms.ModelForm):
    class Meta:
        model = Acompaniante
        fields = [
            'name',
        ]
        labels = {
            'name': 'Name',
        }