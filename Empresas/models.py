from django.db import models

# Create your models here.
class Empresas(models.Model):
    CodEmp = models.IntegerField()
    NomEmp = models.CharField(max_length=100)
    NitEmp = models.CharField(max_length=100)
    DesEmp = models.TextField()

class Cargo(models.Model):
    CodCar = models.IntegerField()
    NomCar = models.CharField(max_length=200)
    Empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE)

class Personal(models.Model):
    CodPer = models.IntegerField()
    NomPer = models.CharField(max_length=200)
    Empresas = models.ForeignKey(Empresas, on_delete=models.CASCADE)
    Cargo   = models.ForeignKey(Cargo, on_delete=models.CASCADE)
