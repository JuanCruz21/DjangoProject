from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Empresas, Cargo,Personal
from django.shortcuts import get_object_or_404

# Create your views here.
def Hello(Saludo):
    return HttpResponse("hello")

def Empresa(request):
    empresa = list(Empresas.objects.values())
    return JsonResponse(empresa, safe=False)

def Cargos(request,CodCar):
    #cargo = Cargo.objects.get(CodCar=CodCar)
    cargo = get_object_or_404(Cargo, CodCar= CodCar)
    return HttpResponse('Cargo: %s' % cargo.NomCar)