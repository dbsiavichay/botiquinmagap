from django.contrib import admin
from .models import *

class TipoProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'edit')
	list_display_links = ('edit',)
	search_fields = ('nombre',)

class GrupoProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'edit')
	list_display_links = ('edit',)
	search_fields = ('nombre',)

class MedidaProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'edit')
	list_display_links = ('edit',)	
	search_fields = ('nombre',)

class ProductoAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'compuesto', 'presentacion', 'precio_referencial', 'registro_sanitario', 'medida', 'edit')	
	list_display_links = ('edit',)
	list_filter = ('tipo', 'grupo',)
	search_fields = ('nombre', 'compuesto', 'presentacion', 'registro_sanitario')

admin.site.register(TipoProducto, TipoProductoAdmin)
admin.site.register(GrupoProducto, GrupoProductoAdmin)
admin.site.register(MedidaProducto, MedidaProductoAdmin)
admin.site.register(Producto, ProductoAdmin)
