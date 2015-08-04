from django.db.models import Q
from django.db.models import Sum
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date
from .serializers import *
from .models import *

class ClienteViewSet(viewsets.ModelViewSet):
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer

	def get_queryset(self):
		queryset = Cliente.objects.all()
		filtro = self.request.QUERY_PARAMS.get('filtro', None)				
		if filtro is not None:
			queryset = queryset.filter(Q(cedula__startswith=filtro)|Q(nombre__icontains=filtro)|Q(apellido__icontains=filtro))		
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
		id_asociacion = self.request.QUERY_PARAMS.get('asociacion', None)
		id_producto = self.request.QUERY_PARAMS.get('producto', None)
		mes = self.request.QUERY_PARAMS.get('mes', None)
		if id_venta is not None:
			queryset = queryset.filter(venta__id=id_venta)
		elif id_asociacion is not None and mes is not None and id_producto is None:
			queryset = queryset.filter(venta__fecha__month=mes, venta__fecha__year=2015, venta__asociacion__id=id_asociacion)
		elif id_asociacion is not None and id_producto is not None and mes is not None:
			fecha = date(2015, int(mes) +1 , 1)			
			queryset = queryset.filter(venta__asociacion__id=id_asociacion, producto__id=id_producto, venta__fecha__lte=fecha)
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