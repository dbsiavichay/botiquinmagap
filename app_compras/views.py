from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class CompraViewSet(viewsets.ModelViewSet):
	queryset = Compra.objects.all()
	serializer_class = CompraSerializer

	def get_queryset(self):
		queryset = Compra.objects.all()		
		id_asociacion = self.request.QUERY_PARAMS.get('asociacion', None)	
		if id_asociacion is not None:
			queryset = queryset.filter(asociacion__id=id_asociacion)
		return queryset

class DetalleCompraViewSet(viewsets.ModelViewSet):
	queryset = DetalleCompra.objects.all()
	serializer_class = DetalleCompraSerializer

	def get_queryset(self):
		queryset = DetalleCompra.objects.all()
		id_compra = self.request.QUERY_PARAMS.get('compra', None)				
		if id_compra is not None:
			queryset = queryset.filter(compra__id=id_compra)
		return queryset