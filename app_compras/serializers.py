from rest_framework import serializers
from .models import *

class DetalleCompraSerializer(serializers.ModelSerializer):
	class Meta:
		model = DetalleCompra
		fields = ('id', 'cantidad','costo_unitario', 'costo_total','producto', 'compra')

class CompraSerializer(serializers.ModelSerializer):	
	detalles = DetalleCompraSerializer(many=True, read_only=True)

	class Meta:
		model = Compra
		fields = ('id', 'fecha','valor_total', 'asociacion', 'detalles')
