from django.contrib import admin
from django.contrib import messages
from .forms import *
from .models import \
    Vehiculo,\
    TipoCombustible,\
    TipoVehiculo,\
    Cliente,\
    Marca,\
    Empleado,\
    Inspeccion,\
    RentaxDevolucion,\
    Modelo
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre','cedula','tipopersona']


class RentaAdmin(admin.ModelAdmin):
    form = RentaForm
    list_display = ['vehiculo','cliente','estado']

class InspeccionAdmin(admin.ModelAdmin):
    exclude = ('estado',)
    list_display = ['vehiculo','cliente','estado']



class VehiculoAdmin(admin.ModelAdmin):
    exclude = ('estado',)
    list_display = ['descripcion','chasis','marca','modelo','estado']


    # def save_model(self, request, obj, form, change):
    #     if 'owner' in form.changed_data:
    #         messages.add_message(request, messages.INFO, 'Car has been sold')
    #     super(InspeccionAdmin, self).save_model(request, obj, form, change)


# Register your models here.
admin.site.register(Vehiculo,VehiculoAdmin)
admin.site.register(TipoCombustible)
admin.site.register(TipoVehiculo)
admin.site.register(Cliente,ClienteAdmin)
admin.site.register(Marca)
admin.site.register(Empleado)
admin.site.register(Inspeccion,InspeccionAdmin)
admin.site.register(RentaxDevolucion,RentaAdmin)
admin.site.register(Modelo)
