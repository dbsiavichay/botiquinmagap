from django.db import models
from app_botiquin.models import Producto
from app_localizacion.models import Asociacion
from app_compras.models import DetalleCompra

class Inventario(models.Model):
	cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)
	valor_unitario = models.DecimalField(max_digits = 7, decimal_places = 2)
	producto = models.ForeignKey(Producto)
	asociacion = models.ForeignKey(Asociacion)

	def get_valor_total(self):
		return self.cantidad * self.valor_unitario

	def edit(self):
		return '<span class="icon-pencil"></a>'

	edit.allow_tags = True

class Caducado(models.Model):
	cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)
	fecha = models.DateField()
	inventario = models.ForeignKey(Inventario)
	detalleCompra = models.ForeignKey(DetalleCompra)

class Kardex(models.Model):
	fecha = models.DateField()
	tipo_transaccion = models.PositiveSmallIntegerField()
	descripcion = models.CharField(max_length = 256)
	cantidad = models.DecimalField(max_digits = 7, decimal_places = 2)
	valor_unitario = models.DecimalField(max_digits = 7, decimal_places = 2)
	saldo = models.DecimalField(max_digits = 7, decimal_places = 2)	
	producto = models.ForeignKey(Producto)
	asociacion = models.ForeignKey(Asociacion)

	def get_transaccion(self):
		if tipo_transaccion == 0:
			return "Entrada"
		else:
			return "Salida"

	def get_total_transaccion(self):
		return self.cantidad * self.valor_unitario

	def get_total_saldo(self):
		return self.saldo * self.valor_unitario

	def edit(self):
		return '<span class="icon-pencil"></a>'

	edit.allow_tags = True