from django import forms
from django.contrib.auth.models import User
from .models import Klasa, Lendet, Lesson



class KlasaForm(forms.ModelForm):
    class Meta:
        model = Klasa
        fields = '__all__'
        help_texts = {
            'titulli': 'Ex. Clase 11 o Clase de Informática',
            'pershkrimi':'Pon una breve descripción de la clase.',
            'imazhi':'Puedes poner una foto de la clase o se puede dejar en blanco'
        }

class LendaForm(forms.ModelForm):
    class Meta:
        model = Lendet
        fields = ['creador','slug', 'titulli', 'klasa', 'pershkrimi', 'imazhi_lendes']
        help_texts = {
            'titulli': 'Ex. Matemáticas, Geografía, etc.',
            'pershkrimi':'Proporcione una breve descripción del tema.',
            'klasa':'Selecciona la clase para la que crearás la asignatura',
            'imazhi_lendes':'Puedes poner una foto del tema o se puede dejar en blanco'
        }
        labels = {
            'titulli':'Título del tema'
        }
        widgets = {'creador': forms.HiddenInput(), 'slug': forms.HiddenInput()}


class MesimiForm(forms.ModelForm):
    class Meta:
        model = Lesson 
        fields = ['slug','titulli', 'lenda', 'video_id', 'pozicioni', ]
        help_texts = {
            'titulli':'Vendosni titullin e mesimit',
            'lenda':'Zgjidhni lenden per te cilen i perket ky mesim',
            'video_id':'Vendosni ID e videos nga Youtube te cilen do te ngarkoni (<a href="/media/youtube_help.png">ku mund ta gjej ID</a>)',
            'pozicioni':'Vendosni numrin e pozicionit ose radhen e mesimit '
        }
        widgets = {
            'slug': forms.HiddenInput()
        }