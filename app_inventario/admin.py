from django.contrib import admin
from .models import *

class CaducadoInline(admin.TabularInline):
	model = Caducado
	extra = 1

class InventarioAdmin(admin.ModelAdmin):
	list_display = ('cantidad', 'producto', 'valor_unitario', 'get_valor_total', 'asociacion', 'edit')
	list_display_links = ('edit',)
	list_filter = ('asociacion',)
	search_fields = ('producto', 'asociacion',)
	inlines = [CaducadoInline,]

class KardexAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'get_transaccion','producto', 'descripcion','cantidad', 'valor_unitario', 'get_total_transaccion', 'saldo','get_total_saldo', 'asociacion', 'edit',)
	list_display_links = ('edit',)
	list_filter = ('asociacion','producto')


admin.site.register(Inventario, InventarioAdmin)	
admin.site.register(Kardex, KardexAdmin)
