from django.db import models

# Create your models here.
class Empresas(models.Model):
    CodEmp = models.IntegerField()
    NomEmp = models.CharField(max_length=100)