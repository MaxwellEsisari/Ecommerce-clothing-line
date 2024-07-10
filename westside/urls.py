
from django.contrib import admin
from django.urls import path,include
from westside import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('cart/', include('cart.urls')),
    path('', include('django.contrib.auth.urls')),  # This line includes Django's built-in authentication URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
