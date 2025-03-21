from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return HttpResponse("Esta es la página de inicio!")

def pagina1(request):
    return HttpResponse("Esta es la página 1!")

def pagina2(request):
    return HttpResponse("Esta es la página 2!")
