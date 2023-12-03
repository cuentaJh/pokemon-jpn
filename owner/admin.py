from django.contrib import admin
from .models import Owner

# Register your models here.

# admin.site.register(Owner)  #1er modelo

@admin.register(Owner)     #2do modelo
class OwnerAdmin(admin.ModelAdmin):
    list_display = ("nombre", "pais", "edad")   # este comando ya no hace caso al __str__ creado en models
    list_filter = ("edad", "pais")   # agregar filtros
    search_fields = ("nombre", "pais")       # agrega un cuadro de busqueda
    #fields = ("edad", "nombre")        #para especificar los campos que se solicitan en el registro y tambien cambiar el orden de los campos



