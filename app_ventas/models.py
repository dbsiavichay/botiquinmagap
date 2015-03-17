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
		return '%s %s' % self.nombre, self.apellido

	edit.allow_tags = True

class Enfermedad(models.Model):
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
	cliente = models.ForeignKey(Cliente)
	asociacion = models.ForeignKey(Asociacion)	

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return 'Cliente: %s, Fecha: %s, Valor: %s' % self.cliente, self.fecha, self.valorTotal

	edit.allow_tags = True

class DetalleVenta(models.Model):
	cantidad = models.DecimalField(max_digits = 5, decimal_places = 2);
	precio_unitario = models.DecimalField(max_digits = 7, decimal_places = 2)
	precio_total = models.DecimalField(max_digits = 9, decimal_places = 2)
	producto = models.ForeignKey(Producto)
	venta = models.ForeignKey(Venta)

	def edit(self):
		return '<span class="icon-pencil"></a>'

	edit.allow_tags = True

class UsoVenta(models.Model):
	cantidad = models.DecimalField(max_digits = 5, decimal_places = 2)
	enfermedad = models.ForeignKey(Enfermedad)
	especie = models.ForeignKey(Especie)
	detalle_venta = models.ForeignKey(DetalleVenta)
