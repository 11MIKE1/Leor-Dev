from django.contrib import admin
from django.urls import path, include, re_path


from django.conf import settings
from django.conf.urls.static import static

from .health_check_api import HealthCheckAPI
from .swagger import schema_view
from .views import (
    MainAPI, API
)

urlpatterns = [
    # healthcheck
    path('healthcheck/', HealthCheckAPI.as_view(), name='api-health-check'),
    # admin
    path('admin/', admin.site.urls),

    # path('api/', include(api_urlpatterns)),
    # auth

    #swagger
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.IMAGE_URL, document_root=settings.IMAGE_ROOT)
