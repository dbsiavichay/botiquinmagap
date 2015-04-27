from django.db import models

class TipoProducto(models.Model):
	class Meta:
		verbose_name = 'tipo de producto'
		verbose_name_plural = 'tipos de producto'

	nombre = models.CharField(max_length = 64)

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return self.nombre

	edit.allow_tags = True

class GrupoProducto(models.Model):
	class Meta:
		verbose_name = 'grupo de producto'
		verbose_name_plural = 'grupos de producto'

	nombre = models.CharField(max_length = 64)	

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return self.nombre

	edit.allow_tags = True

class MedidaProducto(models.Model):
	class Meta:
		verbose_name = 'medida de producto'
		verbose_name_plural = 'medidas de producto'

	nombre = models.CharField(max_length = 64)	

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return self.nombre

	edit.allow_tags = True

class Producto(models.Model):
	class Meta:
		verbose_name = 'producto'
		verbose_name_plural = 'productos'

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
