from rest_framework import serializers
from viajes.models import Cliente, Reserva, Viaje, Destino, AuthUser

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ('first_name','last_name','username','email','password')


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ('idcliente','usuario')

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





