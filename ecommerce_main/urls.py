from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ecommerce_product.urls')),
    path('', include('ecommerce_about.urls')),
    path('', include('ecommerce_contact.urls')),
    path('accounts/', include('ecommerce_account.urls')),
]

# /////////////////// config static ///////////////////
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
