from django.shortcuts import render
from django.http import HttpResponse
from .models import  Jugador

#Para el login
from AppInicio.forms import JugadorFormulario, UserRegisterForm, UserEditForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    return render(request,"AppInicio/inicio.html")

def calendario(request):
    return render(request,"AppInicio/calendario.html")

def comenta(request):
    return render(request,"AppInicio/comenta.html")

def comparte(request):
    return render(request,"AppInicio/comparte.html")

def estadios(request):
    return render(request,"AppInicio/estadios.html")

def grupos(request):
    return render(request,"AppInicio/grupos.html")

def invita(request):
    return render(request,"AppInicio/invita.html")

def miequipo(request):
    return render(request,"AppInicio/miequipo.html")

def mimundial(request):
    return render(request,"AppInicio/mimundial.html")

def mispredicciones(request):
    return render(request,"AppInicio/mispredicciones.html")

def paises(request):
    return render(request,"AppInicio/paises.html")

def jugadores(request):
    return render(request,"AppInicio/jugadores.html")

def resultados(request):
    return render(request,"AppInicio/resultados.html")
    
def sobrenos(request):
    return render(request,"AppInicio/sobrenos.html")

'''
JUGADOR
'''
@login_required
def jugadorFormulario(request):
    jugadores=Jugador.objects.all()
    
    if request.method =='POST':
        miFormulario=JugadorFormulario(request.POST)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            nombre=info.get("nombre")
            apellido=info.get("apellido")
            edad=info.get("edad")
            pais=info.get("pais")
            equipo=info.get("equipo")
            posicion=info.get("posicion")
            jugador = Jugador(nombre=nombre, apellido=apellido, edad=edad, pais=pais, equipo=equipo, posicion=posicion)
            jugador.save()
            return render(request,"AppInicio/jugadorFormulario.html",{"mensaje": "Jugador creado, puede crear otro","formulario":miFormulario,"jugador":jugador.apellido,"jugadores":jugadores})
        else:
            return render(request,"AppInicio/jugadorFormulario.html",{"mensaje": "ERROR","formulario":miFormulario,"jugadores":jugadores})

    else:
        miFormulario=JugadorFormulario()
        return render(request,"AppInicio/jugadorFormulario.html",{"formulario":miFormulario,"jugadores":jugadores})
    return render(request,"AppInicio/jugadorFormulario.html",contexto)



'''
LOGIN
'''

def login_request(request):

    if request.method=="POST":
        form = AuthenticationForm (request,data=request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user=authenticate (username=usuario, password=contra)

            if user is not None:
                login(request, user)
                return render(request,"AppInicio/inicio.html",{"mensaje":f"Bienvenido {usuario} "})
            else:
                return render (request,"AppInicio/inicio.html",{"mensaje":"Error, datos incorrectos"})
        
        else:
            return render(request,"AppInicio/inicio.html",{"mensaje":"Error, formulario erroneo"})
    
    form=AuthenticationForm()

    return render (request, "AppInicio/login.html", {'form':form})

'''
REGISTER
'''
def register(request):
    if request.method=="POST":
        form= UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            email=form.cleaned_data["email"]
            if User.objects.filter(email=email).exists():
                return render(request, "AppInicio/registro.html", {"form":form, "mensaje":f"{email} ya está en uso"})
            form.save()
            return render(request, "AppInicio/inicio.html", {"mensaje":f"Usuario {username} creado!"})
        else:
            return render(request, "AppInicio/registro.html", {"form":form, "mensaje":"Uno de los campos ya existe o es inválido"})
    else:
        form=UserRegisterForm()
    return render(request, "AppInicio/registro.html", {"form":form})




'''
EDITAR PERFIL
'''
@login_required
def editarPerfil(request):

    usuario=request.user

    if request.method=="POST":
        miFormulario=UserEditForm(request.POST)
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2= informacion['password2']
            usuario.save()

            return  render(request, "AppInicio/inicio.html")
    else:
        miFormulario=UserEditForm(initial={"email":usuario.email})
        
    return render(request, "AppInicio/editarPerfil.html",{"miFormulario":miFormulario, "usuario":usuario})