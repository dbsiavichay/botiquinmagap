from rest_framework import serializers
from .models import *

class InventarioSerializer(serializers.ModelSerializer):
	valor_total = serializers.SerializerMethodField()

	class Meta:
		model = Inventario
		fields = ('id', 'cantidad', 'valor_unitario', 'valor_total', 'producto', 'asociacion')

	def get_valor_total(self, obj):
		return obj.cantidad * obj.valor_unitario

class CaducadoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Caducado
		fields = ('id', 'cantidad', 'fecha', 'inventario', 'detalle_compra',)

class KardexSerializer(serializers.ModelSerializer):	
	valor_total = serializers.SerializerMethodField()
	total = serializers.SerializerMethodField()

	class Meta:
		model = Kardex
		fields = ('id', 'fecha', 'tipo_transaccion', 'descripcion', 'cantidad', 'valor_unitario', 'valor_total','saldo', 'total', 'producto', 'asociacion',)

	def get_valor_total(self, obj):
		return obj.cantidad * obj.valor_unitario

	def get_total(self, obj):
		return obj.saldo * obj.valor_unitario