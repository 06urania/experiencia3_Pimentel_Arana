from django.urls import path
from . import views
from .views import index_view, reserva_view, nosotros_view, login_view, registro_view, lista_paquetes, crear_reserva

urlpatterns = [
      path('', views.index, name='index'),
    path('reserva/', views.reserva, name='reserva'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.login, name='login'),
    path('', index_view, name='index'),
    path('reserva/', reserva_view, name='reserva'),
    path('nosotros/', nosotros_view, name='nosotros'),
    path('registro/', registro_view, name='registro'),
    path('login/', login_view, name='login'),
    path('lista_paquetes/', lista_paquetes, name='lista_paquetes'),
    path('crear_reserva/', crear_reserva, name='crear_reserva'),
    path('registro/', views.registro_usuario, name='registro'),
]
