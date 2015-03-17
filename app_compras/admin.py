from django.contrib import admin
from .models import *

class DetalleCompraInline(admin.TabularInline):
	model = DetalleCompra
	extra = 1
	
class CompraAdmin(admin.ModelAdmin):
	list_display = ('asociacion','fecha', 'valor_total', 'edit',)
	list_display_links = ('edit',)
	list_filter = ('asociacion',)
	search_fields = ('asociacion__nombre', 'fecha',)
	inlines = [DetalleCompraInline,]


# class DetalleCompraAdmin(admin.ModelAdmin):
# 	list_display = ('compra', 'producto', 'cantidad', 'costo_unitario', 'costo_total', 'edit',)
# 	list_display_links = ('edit',)	
# 	search_fields = ('producto',)		


admin.site.register(Compra, CompraAdmin)
# admin.site.register(DetalleCompra, DetalleCompraAdmin)
