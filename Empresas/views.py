from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Hello(Saludo):
    return HttpResponse("hello")
