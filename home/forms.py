from django.forms import ModelForm
from .models import *
class Cursoform(ModelForm):
    class Meta:
        model=Curso
        fields=["codigo","nombre","creditos","docente"]
        
class Carreraform(ModelForm):
    class Meta:
        model=Carrera
        fields=["codigo","nombre","duracion"]