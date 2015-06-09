from rest_framework import serializers
from app_ventas.models import *
import json

class ClienteSerializer(serializers.ModelSerializer):
	nombre_completo = serializers.SerializerMethodField()

	class Meta:
		model = Cliente
		fields = ('id', 'cedula', 'nombre', 'apellido', 'nombre_completo')

	def get_nombre_completo(self, obj):
		return '{0} {1}'.format(obj.nombre, obj.apellido)

class EnfermedadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Enfermedad
		fields = ('id', 'nombre',)

class EspecieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Especie
		fields = ('id', 'nombre',)

class VentaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Venta
		fields = ('id', 'fecha', 'valor_total', 'cliente', 'asociacion')	

class DetalleVentaSerializer(serializers.ModelSerializer):	
	class Meta:
		model = DetalleVenta
		fields = ('id', 'cantidad','precio_unitario', 'precio_total', 'producto', 'venta')

class UsoVentaSerializer(serializers.ModelSerializer):
	class Meta:
		model = UsoVenta
		fields = ('id', 'cantidad', 'enfermedad', 'especie', 'detalle_venta')