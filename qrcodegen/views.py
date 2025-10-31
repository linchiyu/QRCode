from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def ativos(request):
    return render(request, "ativos.html")


def inativos(request):
    return render(request, "inativos.html")
