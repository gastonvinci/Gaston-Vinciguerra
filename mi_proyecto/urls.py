
from django.contrib import admin
from django.urls import path, include  # Incluimos 'include' para enlazar las URLs de la app

urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el panel de administración
    path('mi_app/', include('mi_app.urls')),  # Enlaza las URLs de la app 'mi_app'
]
