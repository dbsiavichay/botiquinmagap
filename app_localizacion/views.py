from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import *
from .models import *

class AsociacionViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Asociacion.objects.all()
	serializer_class = AsociacionSerializer

	def get_queryset(self):
		queryset = Asociacion.objects.all()
		id_sector = self.request.QUERY_PARAMS.get('sector', None)
		id_tecnico = self.request.QUERY_PARAMS.get('tecnico',None)
		if id_sector is not None and id_tecnico is not None:
			queryset = queryset.filter(sector__id=id_sector, tecnico__id=id_tecnico)
		elif id_sector is not None:
			queryset = queryset.filter(sector__id=id_sector)
		elif id_tecnico is not None:
			queryset = queryset.filter(tecnico__id=id_tecnico)
		return queryset	

class SectorViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Sector.objects.all()
	serializer_class = SectorSerializer

	def get_queryset(self):
		queryset = Sector.objects.all()
		id_parroquia = self.request.QUERY_PARAMS.get('parroquia',None)
		if id_parroquia is not None:
			queryset = queryset.filter(parroquia__id=id_parroquia)
		return queryset

class ParroquiaViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Parroquia.objects.all()
	serializer_class = ParroquiaSerializer

	def get_queryset(self):
		queryset = Parroquia.objects.all()
		id_canton = self.request.QUERY_PARAMS.get('canton', None)
		if id_canton is not None:
			queryset = queryset.filter(canton__id=id_canton)
		return queryset

class CantonViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Canton.objects.all()
	serializer_class = CantonSerializer

	def get_queryset(self):
		queryset = Canton.objects.all()
		id_provincia = self.request.QUERY_PARAMS.get('provincia', None)
		if id_provincia is not None:
			queryset = queryset.filter(provincia__id=id_provincia)
		return queryset

class ProvinciaViewSet(viewsets.ReadOnlyModelViewSet):
	queryset = Provincia.objects.all()
	serializer_class = ProvinciaSerializer