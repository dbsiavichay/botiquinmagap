from django.db import models
from app_botiquin.models import Producto
from app_localizacion.models import Asociacion
from app_compras.models import DetalleCompra

class Inventario(models.Model):
	cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)
	valor_unitario = models.DecimalField(max_digits = 7, decimal_places = 2)
	es_inicial = models.BooleanField(default=False)
	cantidad_inicial = models.DecimalField(max_digits = 7, decimal_places = 2, default=0)
	producto = models.ForeignKey(Producto)
	asociacion = models.ForeignKey(Asociacion)

	def get_valor_total(self):
		return self.cantidad * self.valor_unitario

	def edit(self):
		return '<span class="icon-pencil"></a>'

	edit.allow_tags = True

class Caducidad(models.Model):
	class Meta:
		verbose_name = 'Caducidad'
		verbose_name_plural = 'Caducidad'

	fecha = models.DateField()
	cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)		
	producto = models.ForeignKey(Producto)
	asociacion = models.ForeignKey(Asociacion)	

	def edit(self):
		return '<span class="icon-pencil"></a>'

	edit.allow_tags = True