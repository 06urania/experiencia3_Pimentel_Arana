from django import forms
from .models import Reserva
from .models import Usuario
from django.contrib.auth.hashers import make_password

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['fecha_llegada', 'hora_llegada', 'fecha_salida', 'hora_salida', 'cantidad_personas']
        widgets = {
            'fecha_llegada': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
            'hora_llegada': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'required': 'required'}),
            'fecha_salida': forms.DateInput(attrs={'class': 'form-control', 'type': 'date', 'required': 'required'}),
            'hora_salida': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time', 'required': 'required'}),
            'cantidad_personas': forms.NumberInput(attrs={'class': 'form-control', 'required': 'required'}),
        }

class RegistroForm(forms.ModelForm):
    contraseña = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ['nombre_usuario', 'email', 'contraseña']

    def save(self, commit=True):
        usuario = super().save(commit=False)
        usuario.contraseña = make_password(self.cleaned_data['contraseña'])
        if commit:
            usuario.save()
        return usuario        