from django.contrib import admin
from .models import *

class CaducidadAdmin(admin.ModelAdmin):
	list_display = ('fecha', 'cantidad', 'producto', 'asociacion', 'edit')
	list_display_links = ('edit',)
	list_filter = ('asociacion',)
	search_fields = ('producto', 'asociacion',)	

class InventarioAdmin(admin.ModelAdmin):
	list_display = ('cantidad', 'producto', 'valor_unitario', 'get_valor_total', 'es_inicial', 'cantidad_inicial','asociacion', 'edit')
	list_display_links = ('edit',)
	list_filter = ('asociacion',)
	search_fields = ('producto', 'asociacion',)	



admin.site.register(Inventario, InventarioAdmin)	
admin.site.register(Caducidad, CaducidadAdmin)
