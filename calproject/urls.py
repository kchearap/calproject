from django.contrib import admin
from django.urls import path, include
from daycal import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('daycal/', include('daycal.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)