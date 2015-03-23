from rest_framework import serializers
from .models import *

class InventarioSerializer(serializers.HyperlinkedModelSerializer):
	valor_total = serializers.SerializerMethodField()

	class Meta:
		model = Inventario
		fields = ('id', 'cantidad', 'valor_unitario', 'valor_total', 'producto', 'asociacion')

	def get_valor_total(self, obj):
		return obj.cantidad * obj.valor_unitario

class CaducadoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Caducado
		fields = ('id', 'cantidad', 'fecha', 'inventario', 'detalle_compra',)

class KardexSerializer(serializers.HyperlinkedModelSerializer):
	transaccion = serializers.SerializerMethodField()
	valor_total = serializers.SerializerMethodField()
	total = serializers.SerializerMethodField()

	class Meta:
		model = Kardex
		fields = ('id', 'fecha', 'transaccion', 'descripcion', 'cantidad', 'valor_unitario', 'valor_total','saldo', 'total', 'producto', 'asociacion',)

	def get_transaccion(self, obj):
		if obj.tipo_transaccion == 0:
			return "Entrada"
		else:
			return "Salida"

	def get_valor_total(self, obj):
		return obj.cantidad * obj.valor_unitario

	def get_total(self, obj):
		return obj.saldo * obj.valor_unitario