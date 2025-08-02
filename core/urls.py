from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.i18n import i18n_patterns
from django.urls import re_path


schema_view = get_schema_view(
   openapi.Info(
      title="Iss Japan API",
      default_version='v1',
      description="Iss Japan Project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="example@gmail.com"),
      license=openapi.License(name="Iss Japan License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('contact/', include('contact.urls')),
]


urlpatterns += i18n_patterns(
    path('products/', include('products.urls')),
    path('faqs/', include('faq.urls')),
    path('services/', include('services.urls')),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



urlpatterns += [
   path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]