from django.contrib import admin
from .models import *

class ProvinciaAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre', 'edit')
	list_display_links = ('edit',)
	search_fields = ('nombre',)

class CantonAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre', 'provincia', 'edit')
	list_display_links = ('edit',)
	list_filter = ('provincia',)
	search_fields = ('nombre',)

class ParroquiaAdmin(admin.ModelAdmin):
	list_display = ('codigo', 'nombre', 'canton', 'edit')
	list_display_links = ('edit',)
	list_filter = ('canton',)
	search_fields = ('nombre',)

class SectorAdmin(admin.ModelAdmin):	
	list_display = ('nombre', 'parroquia', 'edit')
	list_display_links = ('edit',)
	list_filter = ('parroquia',)
	search_fields = ('nombre',)

class AsociacionAdmin(admin.ModelAdmin):
	list_display = ('nombre', 'responsable', 'latitud', 'longitud', 'sector', 'tecnico', 'edit',)
	list_display_links = ('edit',)
	list_filter = ('sector', 'tecnico',)
	search_fields = ('nombre', 'responsable',)

admin.site.register(Provincia, ProvinciaAdmin)
admin.site.register(Canton, CantonAdmin)
admin.site.register(Parroquia, ParroquiaAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Asociacion, AsociacionAdmin)

