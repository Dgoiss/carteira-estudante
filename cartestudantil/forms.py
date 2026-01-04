from django import forms
from .models import CarteiraEstudante

class CarteiraForm(forms.ModelForm):
    class Meta:
        model = CarteiraEstudante
        fields = ['nome_completo', 'curso', 'matricula', 'data_nascimento', 'foto', 'validade']
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'validade': forms.DateInput(attrs={'type': 'date'}),
        }