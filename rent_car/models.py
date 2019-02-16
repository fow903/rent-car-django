from django.db import models
from .db_views import DBViewRedirectedSave
from django.core.exceptions import ValidationError
Persona_Tipo = (
    ('fiscal', 'Juridica'),
    ('final', 'Fisica'),
)

# Create your models here.



class TipoVehiculo(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "Tipo: "+ self.descripcion


class Marca(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "Marca: " + self.descripcion


class Modelo(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "Modelo " + self.descripcion


class TipoCombustible(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "Combustible: " + self.descripcion


class Vehiculo(models.Model):
    descripcion = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)
    chasis = models.CharField(max_length=255)
    motor = models.CharField(max_length=255)
    placa = models.CharField(max_length=255)
    tipovehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.PROTECT)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT)
    tipocombustible = models.ForeignKey(TipoCombustible, on_delete=models.PROTECT)

    def __str__(self):
        return "Vehiculo: " + self.descripcion + " " + self.chasis


class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    cedula = models.CharField(max_length=255)
    tarjetacredito = models.CharField(max_length=255)
    limitecredito = models.FloatField()
    tipopersona = models.CharField(max_length=12,choices=Persona_Tipo)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "Cliente: " + self.nombre + " " + self.cedula


class Empleado(models.Model):
    nombre = models.CharField(max_length=255)
    cedula = models.CharField(max_length=255)
    tandalabor = models.CharField(max_length=255)
    porc_com = models.FloatField()
    fechaingreso = models.DateField(auto_now=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return "Empleado: " + self.nombre + " " + self.cedula


class Inspeccion(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    tiene_rayaduras = models.BooleanField(default=False)
    tiene_goma_repuesta = models.BooleanField(default=False)
    tiene_gato = models.BooleanField(default=False)
    tiene_roturas_cristal = models.BooleanField(default=False)
    estado_gomas = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now=True)
    cantidad_combustible = models.CharField(max_length=10)
    estado = models.BooleanField(default=True)
    # rentaxdevolucion = models.ForeignKey('RentaxDevolucion', on_delete=models.PROTECT)

    def save(self, *args,**kwargs):
        renta = RentaxDevolucion.objects.filter(estado=True,vehiculo_id=self.vehiculo_id)
        res = super(Inspeccion, self).save(*args,**kwargs)
        if renta:
            inspeccion = self.__class__.objects.filter(vehiculo_id=self.vehiculo_id,estado=True)
            if self.estado == True:
                print("Estado era True")
                if len(inspeccion) > 1:
                    print("Desarchivando Vehiculo")
                    inspeccion.update(estado=False)
                    self.vehiculo.estado = True
                    self.vehiculo.save()
                    self.estado = False
                    renta.update(estado=False)
                elif len(inspeccion) <=1:
                    print("Archivando Vehiculo")
                    self.vehiculo.estado = False
                    self.vehiculo.save()

            return res

    def clean(self):
        renta = RentaxDevolucion.objects.filter(estado=True,vehiculo_id=self.vehiculo_id)
        inspeccion = self.__class__.objects.filter(estado=True,vehiculo_id=self.vehiculo_id)

        if not self.id:
            if len(renta) > 0:
                if self.cliente_id == renta[0].cliente_id:
                    pass
                else:
                    raise ValidationError("Este cliente no tiene este vehiculo rentado")

        if len(renta) == 0:
            raise ValidationError("Debe Crear el registro de Renta X Devolucion")


    def __str__(self):
        return "Inspección: " + self.vehiculo.descripcion + " " + str(self.fecha)


class RentaxDevolucion(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.PROTECT)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    fecha_renta = models.DateTimeField(auto_now=True)
    fecha_devolucion = models.DateTimeField()
    montoxdia = models.FloatField()
    cantidad_dias = models.IntegerField()
    comentario = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    # def save(self, *args,**kwargs):
    #     renta = self.__class__.objects.filter(vehiculo_id=self.vehiculo_id,estado=True)
    #     if len(self.__class__.objects.filter(vehiculo_id=self.vehiculo_id)) > 0:
    #         renta[0].estado = False
    #         self.vehiculo.estado = True
    #         self.estado = False

        # return super(RentaxDevolucion, self).save(*args,**kwargs)

    def __str__(self):
        return "Renta/Devolucion: " + self.vehiculo.descripcion + " " + self.cliente.nombre + " " + str(self.fecha_renta)



##################
#VISTAS
##################
#
# class RentxReport(DBViewRedirectedSave,models.Model):
#     fecha =
#     @classmethod
#     def get_sql(self):
#         sql = """
#            CREATE OR REPLACE VIEW dbv_totalesafi AS
#
#
#
#
#            """