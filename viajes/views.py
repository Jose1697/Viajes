from rest_framework.generics import CreateAPIView
from django.shortcuts import render
from rest_framework import generics, permissions
from viajes.models import Cliente, Destino, Reserva, Viaje, AuthUser, Lugar, AuthtokenToken
from django.contrib.auth.models import User
from viajes.serializers import  DestinoSerializer, ReservaSerializer, ViajeSerializer, ClienteSerializer,UserSerializer, LugarSerializer, AdminSerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CreateUserView(CreateAPIView):
    model = User()
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class UserList(generics.ListCreateAPIView):
        queryset = User.objects.all()
        permission_classes = [
                permissions.AllowAny # Or anon users can't register
        ]
        serializer_class = UserSerializer
        # authentication_classes = (TokenAuthentication,)
        # permission_classes = (IsAuthenticated,)

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer

class ClienteList(generics.ListCreateAPIView):
        queryset = Cliente.objects.all()
        serializer_class = ClienteSerializer

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Cliente.objects.all()
        serializer_class = ClienteSerializer

class DestinoList(generics.ListCreateAPIView):
        queryset = Destino.objects.all()
        serializer_class = DestinoSerializer

class DestinoDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Destino.objects.all()    
        serializer_class = DestinoSerializer

class ReservaList(generics.ListCreateAPIView):
        queryset = Reserva.objects.all()
        serializer_class = ReservaSerializer

class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Reserva.objects.all()
        serializer_class = ReservaSerializer

class ViajeList(generics.ListCreateAPIView):
        queryset = Viaje.objects.all()
        serializer_class = ViajeSerializer

class ViajeDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Viaje.objects.all()
        serializer_class = ViajeSerializer

class LugarList(generics.ListCreateAPIView):
        queryset = Lugar.objects.all()
        serializer_class = LugarSerializer

class LugarDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = Lugar.objects.all()
        serializer_class = LugarSerializer

class AdminList(generics.ListCreateAPIView):
        queryset = AuthtokenToken.objects.all()
        serializer_class = AdminSerializer

class AdminDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = AuthtokenToken.objects.all()
        serializer_class = AdminSerializer






