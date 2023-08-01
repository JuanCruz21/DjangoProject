from django.contrib import admin
from .models import Empresas,Cargo,Personal
# Register your models here.

admin.site.register(Empresas)
admin.site.register(Cargo)
admin.site.register(Personal)