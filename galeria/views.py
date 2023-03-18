from django.shortcuts import render

def index (request):
    return render(request, 'galeria/index.html', {'lista': [1, 2, 3, 4, 'tel', True]})

def imagem (request):
    return render(request, 'galeria/imagem.html')

