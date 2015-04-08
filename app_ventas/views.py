from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from .models import *

class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer

	def get_queryset(self):
		queryset = Cliente.objects.all()
		cedula = self.request.QUERY_PARAMS.get('cedula', None)		
		nombre = self.request.QUERY_PARAMS.get('nombre', None)
		apellido = self.request.QUERY_PARAMS.get('apellido', None)
		if cedula is not None:
			queryset = queryset.filter(cedula__startswith=cedula)
		elif nombre is not None:
			queryset = queryset.filter(nombre__contains=nombre)
		elif apellido is not None:
			queryset = queryset.filter(apellido__contains=apellido)
		return queryset	

class EnfermedadViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Enfermedad.objects.all()
	serializer_class = EnfermedadSerializer

class EspecieViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Especie.objects.all()
	serializer_class = EspecieSerializer

class VentaViewSet(viewsets.ModelViewSet):
	queryset = Venta.objects.all()
	serializer_class = VentaSerializer

	def get_queryset(self):
		queryset = Venta.objects.all()
		id_cliente = self.request.QUERY_PARAMS.get('cliente', None)
		id_asociacion = self.request.QUERY_PARAMS.get('asociacion', None)
		id_tecnico = self.request.QUERY_PARAMS.get('tecnico', None)
		if id_cliente is not None and id_asociacion is not None:
			queryset = queryset.filter(cliente__id=id_cliente, asociacion__id=id_asociacion)
		elif id_asociacion is not None:
			queryset = queryset.filter(asociacion__id=id_asociacion)
		elif id_tecnico is not None:
			queryset = queryset.filter(asociacion__tecnico__id=id_tecnico)
		return queryset

class DetalleVentaViewSet(viewsets.ModelViewSet):
	queryset = DetalleVenta.objects.all()
	serializer_class = DetalleVentaSerializer

	def get_queryset(self):
		queryset = DetalleVenta.objects.all()
		id_venta = self.request.QUERY_PARAMS.get('venta', None)				
		if id_venta is not None:
			queryset = queryset.filter(venta__id=id_venta)
		return queryset

class UsoVentaViewSet(viewsets.ModelViewSet):
	queryset = UsoVenta.objects.all()
	serializer_class = UsoVentaSerializer

	def get_queryset(self):
		queryset = UsoVenta.objects.all()
		id_detalle_venta = self.request.QUERY_PARAMS.get('detalleventa', None)				
		if id_detalle_venta is not None:
			queryset = queryset.filter(detalle_venta__id=id_detalle_venta)
		return queryset
