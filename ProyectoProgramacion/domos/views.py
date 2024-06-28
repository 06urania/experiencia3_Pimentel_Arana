from django.shortcuts import render, get_object_or_404, redirect
from django.conf import settings
from .models import Paquete, Reserva
from .form import ReservaForm, RegistroForm
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'domos/index.html')

def nosotros(request):
    return render(request, 'domos/nosotros.html')

def reserva(request):
    return render(request, 'domos/reserva.html')

def registro(request):
    return render(request, 'domos/registro.html')

def login(request):
    return render(request, 'domos/login.html')

def common_context():
    return {
        'background_image_url': settings.BACKGROUND_IMAGE_URL
    }

def index_view(request):
    context = common_context()
    return render(request, 'index.html', context)

def reserva_view(request):
    context = common_context()
    return render(request, 'reserva.html', context)

def nosotros_view(request):
    context = common_context()
    return render(request, 'nosotros.html', context)

def login_view(request):
    context = common_context()
    return render(request, 'login.html', context)

def registro_view(request):
    context = common_context()
    return render(request, 'registro.html', context)

def lista_paquetes(request):
    paquetes = Paquete.objects.all()
    return render(request, 'reservas/reserva.html', {'paquetes': paquetes})

@login_required
def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.usuario = request.user
            reserva.save()
            return redirect('reserva.html')
    else:
        form = ReservaForm()
    return render(request, 'reserva.html', {'form': form})

def registro_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirige al usuario a la página de inicio de sesión después del registro
    else:
        form = RegistroForm()
    return render(request, 'registro.html', {'form': form})