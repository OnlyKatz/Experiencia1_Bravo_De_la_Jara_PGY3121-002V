from rest_framework import serializers 
from core.models import Formulario
class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = ['nombre','apellido','correo','rut','telefono','ciudad','comentario']
        
        