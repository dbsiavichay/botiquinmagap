from django.db import models
from app_localizacion.models import Asociacion
from app_botiquin.models import Producto

class Compra(models.Model):
	fecha = models.DateField()
	valor_total = models.DecimalField(max_digits = 9, decimal_places = 2)
	asociacion = models.ForeignKey(Asociacion)

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return 'Fecha: %s, Valor: %s' % self.fecha, self.valor_total

	edit.allow_tags = True

class DetalleCompra(models.Model):
	class Meta:
		verbose_name = 'detalle de compra'
		verbose_name_plural = 'detalles de compra'

	cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)
	costo_unitario = models.DecimalField(max_digits = 7, decimal_places = 2)
	costo_total = models.DecimalField(max_digits = 9, decimal_places = 2)
	producto = models.ForeignKey(Producto)
	compra = models.ForeignKey(Compra)

	def edit(self):
		return '<span class="icon-pencil"></a>'

	edit.allow_tags = True


