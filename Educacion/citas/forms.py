from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = [
            'acompaniante',
            'fecha',
            'hora',
            #'dateTime',
        ]

        labels = {
            'acompaniante' : 'Acompaniante',
            'fecha' : 'Fecha',
            'hora' : 'Hora',
            #'dateTime' : 'Date Time',
        }
