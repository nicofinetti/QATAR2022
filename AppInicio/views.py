from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime


def inicio(request):
    return render(request,"AppInicio/inicio.html")

def calendario(request, anio = datetime.now().year, mes = datetime.now().month):

    #creamos calendario

    cal = HTMLCalendar().formatmonth(anio, mes)

    #para obtener fecha actual

    now = datetime.now()
    actual = now.month

    #para obtener tiempo actual especifico

    tiempo = now.strftime('%H:%M')

    return render(request, 'AppInicio/calendario.html', {
        "anio": anio,
        "mes": mes,
        "cal": cal,
        "actual": actual,
        "tiempo": tiempo,
    })

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





