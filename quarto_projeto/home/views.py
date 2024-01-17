from django.shortcuts import render
from django.http import HttpResponse

def meu_home(request):
    return HttpResponse('<head><style>body{ background-color: black; display: flex; align-items: center; justify-content: center;}</style></head> <body><h1 style="color: green">MEU PRIMEIRO WEB APP</h1></body>')
