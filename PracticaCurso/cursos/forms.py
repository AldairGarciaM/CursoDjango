from django import forms
from .models import comentarioContacto
from .models import Archivos
from django.forms import ModelForm, ClearableFileInput

class comentarioContactoForm(forms.ModelForm):
    class Meta:
        model= comentarioContacto
        fields = ['nombre', 'correo' , 'curos', 'comentario']

class CustomCleareFlied(ClearableFileInput):
    template_with_clear='<br><label for= "%(clear_checkbox_id)s">%(clear_checkbox_label)s </label>%(clear)s'

class formArchivo(ModelForm):
    class Meta:
        model= Archivos
        fields=('titulo', 'descripcion', 'archivo')
        widgets={ 'archivo': CustomCleareFlied}