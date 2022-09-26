from django.shortcuts import render

def login(request):
    return render(request, '../templates/GestionUsuario/login.html', {})