from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *	

class TipoProductoViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = TipoProducto.objects.all()
	serializer_class = TipoProductoSerializer

class GrupoProductoViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = GrupoProducto.objects.all()
	serializer_class = GrupoProductoSerializer

class MedidaProductoViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = MedidaProducto.objects.all()
	serializer_class = MedidaProductoSerializer

class ProductoViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Producto.objects.all()
	serializer_class = ProductoSerializer

	def get_queryset(self):
		queryset = Producto.objects.all()
		id_medida = self.request.QUERY_PARAMS.get('medida',None)
		id_tipo = self.request.QUERY_PARAMS.get('tipo', None)
		id_grupo = self.request.QUERY_PARAMS.get('grupo',None)
		if id_medida is not None and id_tipo is not None and id_grupo is not None:
			queryset = queryset.filter(medida__id=id_medida, tipo__id=id_tipo, grupo__id=id_grupo)
		elif id_medida is not None and id_tipo is not None:
			queryset = queryset.filter(medida__id=id_medida, tipo__id=id_tipo)
		elif id_medida is not None and id_grupo is not None:
			queryset = queryset.filter(medida__id=id_medida, grupo__id=id_grupo)
		elif id_tipo is not None and id_grupo is not None:
			queryset = queryset.filter(tipo__id=id_tipo, grupo__id=id_grupo)
		elif id_medida is not None :
			queryset = queryset.filter(medida__id=id_medida)
		elif id_tipo is not None:
			queryset = queryset.filter(tipo__id=id_tipo)
		elif id_grupo is not None:
			queryset = queryset.filter(grupo__id=id_grupo)
		return queryset