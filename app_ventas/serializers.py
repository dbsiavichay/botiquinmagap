from rest_framework import serializers
from app_ventas.models import *
from app_localizacion.serializers import AsociacionSerializer
import json

class ClienteSerializer(serializers.ModelSerializer):
	nombre_completo = serializers.SerializerMethodField()

	class Meta:
		model = Cliente
		fields = ('id', 'cedula', 'nombre', 'apellido', 'nombre_completo')

	def get_nombre_completo(self, obj):
		return '%s %s' % (obj.nombre, obj.apellido)

class EnfermedadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Enfermedad
		fields = ('id', 'nombre',)

class EspecieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Especie
		fields = ('id', 'nombre',)

class UsoVentaSerializer(serializers.ModelSerializer):
	class Meta:
		model = UsoVenta
		fields = ('id', 'cantidad', 'enfermedad', 'especie', 'detalle_venta')

class DetalleVentaSerializer(serializers.ModelSerializer):	
	usos = UsoVentaSerializer(many=True, read_only=True)

	class Meta:
		model = DetalleVenta
		fields = ('id', 'cantidad','precio_unitario', 'precio_total', 'producto', 'venta', 'usos')

class VentaSerializer(serializers.ModelSerializer):	
	detalles = DetalleVentaSerializer(many=True, read_only=True)

	class Meta:
		model = Venta
		fields = ('id', 'fecha', 'valor_total', 'cliente','asociacion', 'detalles')	

