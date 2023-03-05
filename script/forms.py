from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ["tipo_factura", "cuit", "detalle_servicio","cantidad_sesiones",]