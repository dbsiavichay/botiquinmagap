from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class InventarioViewSet(viewsets.ModelViewSet):
	queryset = Inventario.objects.all()
	serializer_class = InventarioSerializer

	def get_queryset(self):
		queryset = Inventario.objects.all()		
		id_asociacion = self.request.QUERY_PARAMS.get('asociacion',None)
		id_producto = self.request.QUERY_PARAMS.get('producto',None)
		if id_asociacion is not None and id_producto is not None:
			queryset = queryset.filter(asociacion__id=id_asociacion, producto__id=id_producto)
		elif id_asociacion is not None:
			queryset = queryset.filter(asociacion__id=id_asociacion)
		return queryset	

class CaducadoViewSet(viewsets.ModelViewSet):
	queryset = Caducado.objects.all()
	serializer_class = CaducadoSerializer

	def get_queryset(self):
		queryset = Caducado.objects.all()
		id_inventario = self.request.QUERY_PARAMS.get('inventario',None)
		if id_inventario is not None:
			queryset = queryset.filter(inventario__id=id_inventario)
		return queryset

class KardexViewSet(viewsets.ModelViewSet):
	queryset = Kardex.objects.all()
	serializer_class = KardexSerializer

	def get_queryset(self):
		queryset = Kardex.objects.all()
		id_asociacion = self.request.QUERY_PARAMS.get('asociacion', None)
		id_producto = self.request.QUERY_PARAMS.get('producto', None)
		if id_asociacion is not None and id_producto is not None:
			queryset = queryset.filter(asociacion__id=id_asociacion, producto__id=id_producto)
		return queryset