from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from app_localizacion.views import *
from app_botiquin.views import *
from app_ventas.views import *
from app_compras.views import *
from app_inventario.views import *

router = routers.DefaultRouter()

router.register(r'localizacion/provincias', ProvinciaViewSet)
router.register(r'localizacion/cantones', CantonViewSet)
router.register(r'localizacion/parroquias', ParroquiaViewSet)
router.register(r'localizacion/sectores', SectorViewSet)
router.register(r'localizacion/asociaciones', AsociacionViewSet)

router.register(r'botiquin/tiposproducto', TipoProductoViewSet)
router.register(r'botiquin/gruposproducto', GrupoProductoViewSet)
router.register(r'botiquin/medidasproducto', MedidaProductoViewSet)
router.register(r'botiquin/productos', ProductoViewSet)

router.register(r'ventas/clientes', ClienteViewSet)
router.register(r'ventas/enfermedades', EnfermedadViewSet)
router.register(r'ventas/especies', EspecieViewSet)
router.register(r'ventas/ventas', VentaViewSet)
router.register(r'ventas/detallesventa', DetalleVentaViewSet)
router.register(r'ventas/usosventa', UsoVentaViewSet)

router.register(r'compras/compras', CompraViewSet)
router.register(r'compras/detallescompra', DetalleCompraViewSet)

router.register(r'inventario/inventarios', InventarioViewSet)
router.register(r'inventario/caducados', CaducadoViewSet)
router.register(r'inventario/kardexs', KardexViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'botiquin_proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
