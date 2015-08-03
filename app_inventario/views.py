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
		inicial = self.request.QUERY_PARAMS.get('inicial', None)

		if id_asociacion is not None and inicial is not None:
			queryset = queryset.filter(asociacion__id=id_asociacion, es_inicial=True)
		elif id_asociacion is not None and id_producto is not None:
			queryset = queryset.filter(asociacion__id=id_asociacion, producto__id=id_producto)				
		elif id_asociacion is not None:
			queryset = queryset.filter(asociacion__id=id_asociacion)
		return queryset	

class CaducidadViewSet(viewsets.ModelViewSet):	
	queryset = Caducidad.objects.all()
	serializer_class = CaducidadSerializer

	def get_queryset(self):
		queryset = Caducidad.objects.all()
		id_asociacion = self.request.QUERY_PARAMS.get('asociacion',None)
		id_producto = self.request.QUERY_PARAMS.get('producto',None)				

		if id_asociacion is not None and id_producto is not None:
			queryset = queryset.filter(asociacion__id=id_asociacion, producto__id=id_producto)
		elif id_asociacion is not None:
			queryset = queryset.filter(asociacion__id=id_asociacion)
			
		return queryset