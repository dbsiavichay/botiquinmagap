from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from rest_framework.authtoken import views
from app_localizacion.views import *
from app_botiquin.views import *
from app_ventas.views import *
from app_compras.views import *
from app_inventario.views import *

router = routers.DefaultRouter()

router.register(r'provincias', ProvinciaViewSet)
router.register(r'cantones', CantonViewSet)
router.register(r'parroquias', ParroquiaViewSet)
router.register(r'sectores', SectorViewSet)
router.register(r'asociaciones', AsociacionViewSet)

router.register(r'tiposproducto', TipoProductoViewSet)
router.register(r'gruposproducto', GrupoProductoViewSet)
router.register(r'medidasproducto', MedidaProductoViewSet)
router.register(r'productos', ProductoViewSet)

router.register(r'clientes', ClienteViewSet)
router.register(r'enfermedades', EnfermedadViewSet)
router.register(r'especies', EspecieViewSet)
router.register(r'ventas', VentaViewSet)
router.register(r'detallesventa', DetalleVentaViewSet)
router.register(r'usosventa', UsoVentaViewSet)

router.register(r'compras', CompraViewSet)
router.register(r'detallescompra', DetalleCompraViewSet)

router.register(r'inventarios', InventarioViewSet)
router.register(r'caducidad', CaducidadViewSet)
router.register(r'usuarios', UserViewSet)

urlpatterns = patterns('',
    # Examples:    
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-token-auth/', views.obtain_auth_token),
)

