from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from AvtoW import settings
from base.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)