from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request,"AppInicio/padre.html")

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

def resultados(request):
    return render(request,"AppInicio/resultados.html")
    
def sobrenos(request):
    return render(request,"AppInicio/sobrenos.html")
