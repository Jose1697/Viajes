from rest_framework import serializers
from django.contrib.auth.models import User
from viajes.models import Cliente, Reserva, Viaje, Destino, Lugar

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            #email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", "first_name", "last_name")




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
        fields = ('idviaje','iddestino','fecha','hora','capacidad')

class LugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugar
        fields = ('idlugar','iddestino','nombre','descripcion','imagen')





