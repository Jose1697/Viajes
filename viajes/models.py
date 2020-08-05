# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    idcliente = models.AutoField(db_column='idCliente', primary_key=True)  # Field name made lowercase.
    nombres = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=30)
    contra = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'Cliente'


class Destino(models.Model):
    iddestino = models.AutoField(db_column='idDestino', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    imagen = models.CharField(max_length=300)
    precio = models.FloatField()

    class Meta:
        managed = False
        db_table = 'Destino'


class Reserva(models.Model):
    idcliente = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='idCliente', primary_key=True)  # Field name made lowercase.
    idviaje = models.ForeignKey('Viaje', models.DO_NOTHING, db_column='idViaje')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Reserva'
        unique_together = (('idcliente', 'idviaje'),)


class Viaje(models.Model):
    idviaje = models.AutoField(db_column='idViaje', primary_key=True)  # Field name made lowercase.
    iddestino = models.ForeignKey(Destino, models.DO_NOTHING, db_column='idDestino', blank=True, null=True)  # Field name made lowercase.
    fecha = models.DateField()
    capacidad = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'Viaje'
