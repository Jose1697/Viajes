from django.contrib import admin
from.models import Cliente
from.models import Viaje
from.models import Destino
from.models import Reserva

admin.site.register(Cliente)
admin.site.register(Destino)
admin.site.register(Viaje)
admin.site.register(Reserva)

