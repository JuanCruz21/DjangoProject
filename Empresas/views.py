from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Empresas, Cargo,Personal
from django.shortcuts import get_object_or_404, render

# Create your views here.
def Hello(Request):
    return render(Request, "index.html")

def Empresa(request):
    #empresa = list(Empresas.objects.values())
    #empresa = get_object_or_404(list(Empresas))
    #return JsonResponse(empresa, safe=False)
    empresas = 'Maggio'
    return render(request, 'Empresas.html',{ 
        'empresas':empresas
    })

def Cargos(request):
    cargos = Cargo.objects.all()
    return render(request, 'Cargo.html',{
        'cargos':cargos
    })
    #cargo = Cargo.objects.get(CodCar=CodCar)
    #cargo = get_object_or_404(Cargo, CodCar= CodCar)
    #return HttpResponse('Cargo: %s' % cargo.NomCar)
def Personal(request):
    #cargo = Cargo.objects.get(CodCar=CodCar)
    #cargo = get_object_or_404(Cargo, CodCar= CodCar)
    #return HttpResponse('Cargo: %s' % cargo.NomCar)
    return render(request, 'Personal.html')