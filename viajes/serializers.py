from rest_framework import serializers
from viajes.models import Cliente, Reserva, Viaje, Destino

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('idcliente','nombres','apellidos','contra')

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ('idcliente','idviaje')


class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = ('iddestino','nombre', 'descripcion', 'imagen', 'precio')

class ViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Viaje
        fields = ('idviaje','iddestino','fecha','capacidad')





