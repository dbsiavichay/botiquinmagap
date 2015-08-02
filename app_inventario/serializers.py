from rest_framework import serializers
from .models import *

class InventarioSerializer(serializers.ModelSerializer):
	valor_total = serializers.SerializerMethodField()

	class Meta:
		model = Inventario
		fields = ('id', 'cantidad', 'valor_unitario', 'valor_total','es_inicial', 'cantidad_inicial','producto', 'asociacion')

	def get_valor_total(self, obj):
		return obj.cantidad * obj.valor_unitario

class CaducidadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Caducidad
		fields = ('id', 'fecha', 'cantidad', 'producto', 'asociacion',)