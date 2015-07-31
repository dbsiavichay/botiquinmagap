from rest_framework import serializers
from app_localizacion.models import Asociacion, Sector, Parroquia, Canton, Provincia
from app_ventas.models import Venta
import json

class ProvinciaSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Provincia
		fields = ('id', 'codigo', 'nombre',)

class CantonSerializer(serializers.ModelSerializer):	
	class Meta:
		model = Canton
		fields = ('id', 'codigo', 'nombre', 'provincia')

class ParroquiaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Parroquia
		fields = ('id', 'codigo', 'nombre', 'canton')

class SectorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Sector
		fields = ('id', 'nombre','parroquia')

class AsociacionSerializer(serializers.HyperlinkedModelSerializer):

	beneficiarios = serializers.SerializerMethodField()
	tecnico = serializers.SerializerMethodField()
	ubicacion = serializers.SerializerMethodField();

	class Meta:
		model = Asociacion
		fields = ('id', 'nombre','responsable', 'latitud', 'longitud', 'beneficiarios','tecnico','ubicacion','sector','observacion')

	def get_beneficiarios(self, obj):
		return Venta.objects.values('cliente__nombre').filter(asociacion = obj).distinct().count()

	def get_tecnico(self, obj):		
		dict_tecnico = {}
		dict_tecnico['username'] = obj.tecnico.username
		dict_tecnico['first_name']= obj.tecnico.first_name
		dict_tecnico['last_name']= obj.tecnico.last_name
		dict_tecnico['email']= obj.tecnico.email
		return json.dumps(dict_tecnico)

	def get_ubicacion(self, obj):
		dict_ubicacion = {}
		dict_ubicacion['sector'] = obj.sector.nombre
		dict_ubicacion['parroquia'] = obj.sector.parroquia.nombre
		dict_ubicacion['canton'] = obj.sector.parroquia.canton.nombre
		dict_ubicacion['provincia'] = obj.sector.parroquia.canton.provincia.nombre
		return json.dumps(dict_ubicacion)

