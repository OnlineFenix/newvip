from django import forms
from .models import NewResult, NewTag
from django.forms import ModelForm


# Define choices as a list of tuples (value, display)
TAG_CHOICES = [
    ('NEW', 'NEW'),
    ('OLD', 'OLD'),
    ('LIVE', 'LIVE'),
    ('TODAY', 'TODAY'),
]
GAME_CHOICES = [
    ('DELHI BAZAR', 'DELHI BAZAR'),
    ('SHRI GANESH', 'SHRI GANESH'),
    ('FARIDABAD', 'FARIDABAD'),
    ('FIROZABAD', 'FIROZABAD'),
    ('GAZIABAD', 'GAZIABAD'),
    ('LAXMI BAZAR', 'LAXMI BAZAR'),
    ('GALI', 'GALI'),
    ('DESAWAR', 'DESAWAR'),
]

class NewResultForm(forms.ModelForm):
    game_name = forms.ChoiceField(choices=GAME_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'background-color: #fff; color: #000; padding: 5px 0; border: 1px double #000; border-radius: 2px; margin-left: 10px;',}))

    class Meta:
        model = NewResult
        fields = ['game_name', 'result']
        widgets = {
            'result': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter result', 'style': 'background-color: #fff; color: #000; padding: 5px 0; border: 1px double #000; border-radius: 2px; margin-left: 10px;',}),
        }

class NewTagForm(forms.ModelForm):
    game_name = forms.ChoiceField(choices=GAME_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'background-color: #fff; color: #000; padding: 5px 0; border: 1px double #000; border-radius: 2px; margin-left: 10px;',}))
    tag = forms.ChoiceField(choices=TAG_CHOICES, widget=forms.Select(attrs={'class': 'form-control', 'style': 'background-color: #fff; color: #000; padding: 5px 0; border: 1px double #000; border-radius: 2px; margin-left: 10px;',}))

    class Meta:
        model = NewTag
        fields = ['game_name', 'tag']