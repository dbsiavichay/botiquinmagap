from rest_framework import serializers
from app_localizacion.models import Asociacion, Sector, Parroquia, Canton, Provincia
from app_ventas.models import Venta
import json

class AsociacionSerializer(serializers.HyperlinkedModelSerializer):

	tecnico = serializers.SerializerMethodField()
	beneficiarios = serializers.SerializerMethodField()

	class Meta:
		model = Asociacion
		fields = ('id', 'nombre','responsable', 'latitud', 'longitud', 'beneficiarios','observacion', 'sector','tecnico')		

	def get_tecnico(self, obj):		
		dict_tecnico = {}
		dict_tecnico['username'] = self.tecnico.username
		dict_tecnico['first_name']= self.tecnico.first_name
		dict_tecnico['last_name']= self.tecnico.last_name
		dict_tecnico['email']= self.tecnico.email
		return json.dumps(dict_tecnico)

	def get_beneficiarios(self, obj):
		return Venta.objects.values('cliente__nombre').filter(asociacion = obj).distinct().count()

class SectorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Sector

class ParroquiaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Parroquia

class CantonSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Canton

class ProvinciaSerializer(serializers.ModelSerializer):
	class Meta:
		model = Provincia