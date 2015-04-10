from rest_framework import serializers
from app_ventas.models import *

class ClienteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cliente
		fields = ('id', 'cedula', 'nombre', 'apellido',)

class EnfermedadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Enfermedad
		fields = ('id', 'nombre',)

class EspecieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Especie
		fields = ('id', 'nombre',)

class VentaSerializer(serializers.HyperlinkedModelSerializer):
	cliente_nombre = serializers.SerializerMethodField()
	asociacion_nombre = serializers.SerializerMethodField();

	class Meta:
		model = Venta
		fields = ('id', 'fecha','valor_total', 'cliente_nombre', 'asociacion_nombre', 'cliente', 'asociacion')

	def get_cliente_nombre(self, obj):
		return obj.cliente.nombre + ' ' + obj.cliente.apellido

	def get_asociacion_nombre(self, obj):
		return obj.asociacion.nombre

class DetalleVentaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DetalleVenta
		fields = ('id', 'cantidad','precio_unitario', 'precio_total','producto', 'venta')

class UsoVentaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = UsoVenta
		fields = ('id', 'cantidad', 'enfermedad', 'especie', 'detalle_venta')