from django.contrib import admin
from django.urls import path, include
from src import urls
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("src.urls"), name="Home")
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
