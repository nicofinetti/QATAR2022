from django.shortcuts import render

def forogeneral(request):
    return render(request, '../templates/ForoNews/forogeneral.html', {})