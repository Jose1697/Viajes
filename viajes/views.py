from django.shortcuts import render
from rest_framework import generics
from viajes.models import Cliente, Destino, Reserva, Viaje, AuthUser
from viajes.serializers import  DestinoSerializer, ReservaSerializer, ViajeSerializer, ClienteSerializer, AuthUserSerializer

class AuthUserList(generics.ListCreateAPIView):
        queryset = AuthUser.objects.all()
        serializer_class = AuthUserSerializer


class AuthUserDetail(generics.RetrieveUpdateDestroyAPIView):
        queryset = AuthUser.objects.all()
        serializer_class = AuthUserSerializer


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


