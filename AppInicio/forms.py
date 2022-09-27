from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class JugadorFormulario(forms.Form):
    nombre=forms.CharField(max_length=50)
    apellido=forms.CharField(max_length=50)
    edad=forms.IntegerField()
    pais=forms.CharField(max_length=50)
    equipo=forms.CharField(max_length=50)
    posicion=forms.CharField(max_length=50)


'''
REGISTRO / EDITAR
'''
class UserRegisterForm(UserCreationForm):

    email= forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
      
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts={k:"" for k in fields}

class UserEditForm(UserCreationForm):
    
    email=forms.EmailField(label="Modificar e-mail")
    password1=forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=["username", "email", "password1", "password2"]
        help_texts={k:"" for k in fields}
