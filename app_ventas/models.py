from django.db import models
from app_localizacion.models import Asociacion
from app_botiquin.models import Producto

class Cliente(models.Model):
	cedula = models.CharField(max_length = 10, unique = True)
	nombre = models.CharField(max_length = 64)
	apellido = models.CharField(max_length = 64)

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return '{0} {1}'.format(self.nombre, self.apellido)

	edit.allow_tags = True

class Enfermedad(models.Model):
	class Meta:
		verbose_name = 'enfermedad'
		verbose_name_plural = 'enfermedades'

	nombre = models.CharField(max_length = 128)

	def edit(self):
		return '<span class="icon-pencil"></a>'	

	def __unicode__(self):
		return self.nombre

	edit.allow_tags = True
			

class Especie(models.Model):
	nombre = models.CharField(max_length = 128)

	def edit(self):
		return '<span class="icon-pencil"></a>'	

	def __unicode__(self):
		return self.nombre

	edit.allow_tags = True

class Venta(models.Model):
	fecha = models.DateField()
	valor_total = models.DecimalField(max_digits = 9, decimal_places = 2)
	cliente = models.ForeignKey(Cliente, related_name='data_cliente')
	asociacion = models.ForeignKey(Asociacion)	

	def __unicode__(self):
		return 'Venta # {0}'.format(self.id)

	def edit(self):
		return '<span class="icon-pencil"></a>'

	edit.allow_tags = True

class DetalleVenta(models.Model):
	class Meta:
		verbose_name = 'detalle de venta'
		verbose_name_plural = 'detalles de venta'

	cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)
	precio_unitario = models.DecimalField(max_digits = 7, decimal_places = 2)
	precio_total = models.DecimalField(max_digits = 9, decimal_places = 2)
	producto = models.ForeignKey(Producto)
	venta = models.ForeignKey(Venta, related_name="detalles")

	def edit(self):
		return '<span class="icon-pencil"></a>'

	edit.allow_tags = True

class UsoVenta(models.Model):
	class Meta:
		verbose_name = 'uso de venta'
		verbose_name_plural = 'usos de venta'

	cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)
	enfermedad = models.ForeignKey(Enfermedad)
	especie = models.ForeignKey(Especie)
	detalle_venta = models.ForeignKey(DetalleVenta, related_name='usos')
