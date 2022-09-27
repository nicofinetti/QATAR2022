from django.forms import ModelForm
from .models import *
 
class CrearEnForo(ModelForm):
    class Meta:
        model= Foro
        fields = "__all__"
 
class CrearEnDiscusion(ModelForm):
    class Meta:
        model= Discusion
        fields = "__all__"