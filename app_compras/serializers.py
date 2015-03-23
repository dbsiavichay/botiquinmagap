from rest_framework import serializers
from .models import *

class CompraSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Compra
		fields = ('id', 'fecha','valor_total', 'asociacion')

class DetalleCompraSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = DetalleCompra
		fields = ('id', 'cantidad','costo_unitario', 'costo_total','producto', 'compra')