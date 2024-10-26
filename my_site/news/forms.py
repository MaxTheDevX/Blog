from .models import Articles
from django.forms import ModelForm, TextInput, Textarea
from django import forms


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article title'
            }),
            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article announcement'
            }),
            "date": forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control',
                'placeholder': 'Date of publication',
            }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text of the article',
            }),
        }
