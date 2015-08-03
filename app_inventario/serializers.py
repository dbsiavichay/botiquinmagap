from rest_framework import serializers
from .models import *
from datetime import date

class InventarioSerializer(serializers.ModelSerializer):
	valor_total = serializers.SerializerMethodField()

	class Meta:
		model = Inventario
		fields = ('id', 'cantidad', 'valor_unitario', 'valor_total','es_inicial', 'cantidad_inicial','producto', 'asociacion')

	def get_valor_total(self, obj):
		return obj.cantidad * obj.valor_unitario

class CaducidadSerializer(serializers.ModelSerializer):
	dias = serializers.SerializerMethodField()

	class Meta:
		model = Caducidad
		fields = ('id', 'fecha', 'cantidad', 'dias', 'producto', 'asociacion',)

	def get_dias(self, obj):
		hoy = date.today()		
		delta = obj.fecha - hoy
		return delta.days