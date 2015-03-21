from rest_framework import serializers
from app_botiquin.models import *

class TipoProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model = TipoProducto
		fields = ('id', 'nombre',)

class GrupoProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model = GrupoProducto
		fields = ('id', 'nombre',)

class MedidaProductoSerializer(serializers.ModelSerializer):
	class Meta:
		model = MedidaProducto
		fields = ('id', 'nombre',)

class ProductoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Producto
		fields = ('id', 'nombre','compuesto','presentacion','precio_referencial','registro_sanitario','medida','tipo','grupo')