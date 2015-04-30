from rest_framework import serializers
from app_ventas.models import *
import json

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
	detalle_producto = serializers.SerializerMethodField()

	class Meta:
		model = DetalleVenta
		fields = ('id', 'cantidad','precio_unitario', 'precio_total', 'detalle_producto', 'producto', 'venta')

	def get_detalle_producto(self, obj):
		dict_producto = {}
		dict_producto['nombre'] = obj.producto.nombre
		dict_producto['compuesto'] = obj.producto.compuesto
		dict_producto['presentacion'] = obj.producto.presentacion
		dict_producto['precio_referencial'] = str(obj.producto.precio_referencial)
		dict_producto['registro_sanitario'] = obj.producto.registro_sanitario
		dict_producto['medida'] = obj.producto.medida.nombre
		dict_producto['tipo'] = obj.producto.tipo.nombre
		dict_producto['grupo'] = obj.producto.grupo.nombre
		return json.dumps(dict_producto)

class UsoVentaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = UsoVenta
		fields = ('id', 'cantidad', 'enfermedad', 'especie', 'detalle_venta')