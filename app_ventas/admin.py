from django.contrib import admin
from .models import *

class ClienteAdmin(admin.ModelAdmin):
	list_display = ('cedula','nombre','apellido', 'edit',)
	list_display_links = ('edit',)
	search_fields = ('cedula', 'nombre', 'apellido',)

class EnfermedadAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'edit')	
	list_display_links = ('edit',)	
	search_fields = ('nombre', )

class EspecieAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'edit')	
	list_display_links = ('edit',)	
	search_fields = ('nombre', )

class VentaAdmin(admin.ModelAdmin):
	list_display = ('cliente', 'fecha', 'valor_total', 'edit',)
	list_display_links = ('edit',)
	list_filter = ('cliente',)
	search_fields = ('cliente__cedula','cliente__nombre', 'cliete__apellido', 'fecha',)

class UsoVentaInline(admin.TabularInline):
	model = UsoVenta
	extra = 1

class DetalleVentaAdmin(admin.ModelAdmin):
	list_display = ('venta', 'producto', 'cantidad', 'precio_unitario', 'precio_total', 'edit',)
	list_display_links = ('edit',)
	list_filter = ('venta',)
	search_fields = ('venta','producto',)
	inlines = [UsoVentaInline,]


admin.site.register(Enfermedad, EnfermedadAdmin)
admin.site.register(Especie, EspecieAdmin)
admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Venta, VentaAdmin)
admin.site.register(DetalleVenta, DetalleVentaAdmin)
