from django.db import models

class TipoProducto(models.Model):
	nombre = models.CharField(max_length = 64)

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return self.nombre

	edit.allow_tags = True

class GrupoProducto(models.Model):
	nombre = models.CharField(max_length = 64)	

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return self.nombre

	edit.allow_tags = True

class MedidaProducto(models.Model):
	nombre = models.CharField(max_length = 64)	

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return self.nombre

	edit.allow_tags = True

class Producto(models.Model):
	nombre = models.CharField(max_length = 128)
	compuesto = models.CharField(max_length = 256, null = True, blank=True)
	presentacion = models.CharField(max_length = 64, null = True, blank=True)
	precio_referencial = models.DecimalField(max_digits = 7, decimal_places = 2, null = True, blank=True)
	registro_sanitario = models.CharField(max_length = 64, null = True, blank=True)
	medida = models.ForeignKey(MedidaProducto)
	tipo = models.ForeignKey(TipoProducto)
	grupo = models.ForeignKey(GrupoProducto)

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return self.nombre

	edit.allow_tags = True
