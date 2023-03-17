from django.shortcuts import render
from django.http import HttpResponse

def index (request):
    return HttpResponse('<h1>Senac no Espaço</h1> <br> <p>sejam bem vindos</p>')