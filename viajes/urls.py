from django.urls import path
from django.conf.urls import url
from . import views
from viajes.views import CreateUserView

from rest_framework.authtoken.views import ObtainAuthToken


urlpatterns = [
    url(r'^cliente$', views.ClienteList.as_view()),
    url(r'cliente/(?P<pk>[0-9]+)$', views.ClienteDetail.as_view()),

    url(r'userscreate',CreateUserView.as_view(), name = "api_create_user"),

    url(r'^users$', views.UserList.as_view()),
    url(r'users/(?P<pk>[0-9]+)$', views.UserDetail.as_view()),

    url(r'^adminauth$', views.AdminList.as_view()),
    url(r'adminauth/(?P<pk>[0-9]+)$', views.AdminDetail.as_view()),

    url(r'^auth/', ObtainAuthToken.as_view()),

    url(r'^destino$', views.DestinoList.as_view()),
    url(r'destino/(?P<pk>[0-9]+)$', views.DestinoDetail.as_view()),

    url(r'^lugar$', views.LugarList.as_view()),
    url(r'lugar/(?P<pk>[0-9]+)$', views.LugarDetail.as_view()),

    url(r'^reserva$', views.ReservaList.as_view()),
    url(r'reserva/(?P<pk>[0-9]+)$', views.ReservaDetail.as_view()),

    url(r'^viaje$', views.ViajeList.as_view()),
    url(r'viaje/(?P<pk>[0-9]+)$', views.ViajeDetail.as_view()),
]