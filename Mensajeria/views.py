from django.shortcuts import render

def mensajes(request):
    return render(request, '../templates/Mensajeria/mensajes.html', {})