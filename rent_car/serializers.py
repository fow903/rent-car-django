from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rent_car.models import *

class TipoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVehiculo
        fields = ('id', 'descripcion', 'estado')


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ('id', 'descripcion', 'estado')


class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        fields = ('id',  'marca', 'descripcion', 'estado')

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     data['marca'] = MarcaSerializer(
    #         Marca.objects.get(pk=data['marca'])).data
    #     return data


class TipoCombustibleSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoCombustible
        fields = ('id', 'descripcion', 'estado')


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ('id', 'descripcion', 'chasis', 'motor', 'chasis', 'tipovehiculo', 'marca', 'modelo', 'tipocombustible', 'estado')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['marca'] = MarcaSerializer(
            Marca.objects.get(pk=data['marca'])).data
        data['modelo'] = ModeloSerializer(
            Modelo.objects.get(pk=data['modelo'])).data
        data['tipocombustible'] = TipoCombustibleSerializer(
            TipoCombustible.objects.get(pk=data['tipocombustible'])).data
        data['tipovehiculo'] = TipoVehiculoSerializer(
            TipoVehiculo.objects.get(pk=data['tipovehiculo'])).data

        return data


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('id', 'nombre','cedula', 'tarjetacredito', 'limitecredito', 'tipopersona', 'estado')


class EmpleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id', 'nombre', 'cedula', 'tandalabor', 'porc_com', 'fechaingreso', 'estado')


class InspeccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspeccion
        fields = ('id', 'vehiculo', 'cliente', 'empleado', 'tiene_rayaduras', 'tiene_goma_repuesta', 'tiene_gato', 'tiene_roturas_cristal', 'estado_gomas', 'fecha', 'cantidad_combustible', 'estado')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['vehiculo'] = VehiculoSerializer(
            Vehiculo.objects.get(pk=data['vehiculo'])).data
        data['cliente'] = ClienteSerializer(
            Cliente.objects.get(pk=data['cliente'])).data
        data['empleado'] = EmpleadoSerializer(
            Empleado.objects.get(pk=data['empleado'])).data

        return data

class RentaxDevolucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RentaxDevolucion
        fields = ('id', 'empelado', 'vehiculo', 'cliente', 'fecha_renta', 'fecha_devolucion', 'montoxdia', 'cantidad_dias', 'comentario', 'estado')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['vehiculo'] = VehiculoSerializer(
            Vehiculo.objects.get(pk=data['vehiculo'])).data
        data['cliente'] = ClienteSerializer(
            Cliente.objects.get(pk=data['cliente'])).data
        data['empleado'] = EmpleadoSerializer(
            Empleado.objects.get(pk=data['empleado'])).data

        return data