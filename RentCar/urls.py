from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from rent_car import views
from django.contrib import admin
from django.views.generic.base import RedirectView

router = routers.DefaultRouter()
router.register(r'tipoveh', views.TipoVehiculoViewSet)
router.register(r'marca', views.MarcaViewSet)
router.register(r'modelo', views.ModeloViewSet)
router.register(r'tipocomb', views.TipoCombustibleViewSet)
router.register(r'vehiculo', views.VehiculoViewSet)
router.register(r'cliente', views.ClienteViewSet)
router.register(r'empleado', views.EmpleadoViewSet)
router.register(r'inspeccion', views.InspeccionViewSet)
router.register(r'rentdev', views.RentaxDevolucionViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('report_builder/', include('report_builder.urls')),
    # path('', include(router.urls)),
    path('', RedirectView.as_view(url='/admin/rent_car')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


