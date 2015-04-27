from django.db import models
from django.contrib.auth.models import User


class Provincia(models.Model):
	codigo = models.CharField(max_length = 32)
	nombre = models.CharField(max_length = 64)

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return self.nombre

	edit.allow_tags = True

class Canton(models.Model):
	class Meta:
		verbose_name = 'canton'
		verbose_name_plural = 'cantones'

	codigo = models.CharField(max_length = 32)
	nombre = models.CharField(max_length = 64)
	provincia = models.ForeignKey(Provincia, on_delete = models.CASCADE)

	def edit(self):
		return '<span class="icon-pencil"></a>'

	edit.allow_tags = True

	def __unicode__(self):
		return self.nombre

class Parroquia(models.Model):
	codigo = models.CharField(max_length = 32)
	nombre = models.CharField(max_length = 64)
	canton = models.ForeignKey(Canton, on_delete = models.CASCADE)

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return self.nombre

	edit.allow_tags = True

class Sector(models.Model):
	class Meta:
		verbose_name = 'sector'
		verbose_name_plural = 'sectores'
	nombre = models.CharField(max_length = 128)
	parroquia = models.ForeignKey(Parroquia, on_delete = models.CASCADE)

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return self.nombre

	edit.allow_tags = True

class Asociacion(models.Model):
	class Meta:
		verbose_name = 'asociacion'
		verbose_name_plural = 'asociaciones'
	nombre = models.CharField(max_length = 128)
	responsable = models.CharField(max_length = 256)
	latitud = models.FloatField(null = True, blank=True)
	longitud = models.FloatField(null = True, blank=True)
	observacion = models.TextField(null = True, blank=True)
	sector = models.ForeignKey(Sector)
	tecnico = models.ForeignKey(User)

	def edit(self):
		return '<span class="icon-pencil"></a>'

	def __unicode__(self):
		return self.nombre

	edit.allow_tags = True
