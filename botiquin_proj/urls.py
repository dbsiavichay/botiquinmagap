from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from app_localizacion.views import *
from app_botiquin.views import *

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

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'botiquin_proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
