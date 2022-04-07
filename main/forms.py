from .models import Accord, Artist
from django.forms import ModelForm, TextInput, Textarea


class ArtistForm(ModelForm):
    class Meta:
        model = Artist
        fields = ['artist_name']
        widgets = {'artist_name': TextInput(attrs={"class": "form-control", 'placeholder': "Исполнитель"}),}


class AccordForm(ModelForm):
    class Meta:
        model = Accord
        fields = ['song_title', 'song_text', 'сhords_used', 'link_to_the_video']
        widgets = {'song_title': TextInput(attrs={"class": "form-control", 'placeholder': "Название произведения"}),
            'song_text': Textarea(attrs={"class": "form-control", 'placeholder': "Текст с аккордами"}),
            'сhords_used': TextInput(attrs={"class": "form-control", 'placeholder': "Используемые аккорды"}),
            'link_to_the_video': TextInput(attrs={"class": "form-control", 'placeholder': "Ссылка на видео"}),
            }