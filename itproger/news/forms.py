from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'date', 'departure', 'full_text']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия Имя Отчество'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата заезда'
            }),
            "departure": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выезда'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Дополнительные пожелания'
            })
        }