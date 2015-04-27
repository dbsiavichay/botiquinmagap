from django.apps import AppConfig

class BotiquinConfig(AppConfig):
	name='app_botiquin'
	verbose_name=u'Botiquin'

class ComprasConfig(AppConfig):
	name='app_compras'
	verbose_name=u'Compras'

class InventarioConfig(AppConfig):
	name='app_inventario'
	verbose_name=u'Inventario'

class LocalizacionConfig(AppConfig):
	name='app_localizacion'
	verbose_name=u'Localizacion'

class VentasConfig(AppConfig):
	name='app_ventas'
	verbose_name=u'Ventas'