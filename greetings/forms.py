from django.forms import ModelForm
from .models import Visitor
from django import forms


class VisitorForm(ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'surname']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': "Введіть ваше ім'я"})
        }
