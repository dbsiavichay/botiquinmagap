from rest_framework import serializers
from .models import *

class CompraSerializer(serializers.ModelSerializer):
	class Meta:
		model = Compra
		fields = ('id', 'fecha','valor_total', 'asociacion')

class DetalleCompraSerializer(serializers.ModelSerializer):
	class Meta:
		model = DetalleCompra
		fields = ('id', 'cantidad','costo_unitario', 'costo_total','producto', 'compra')