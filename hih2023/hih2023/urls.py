from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='main')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration/', views.registration_view, name='registration'),
    path('change_password/', views.change_password, name='change_password'),
    path('perms/', views.permissions, name='perms')
]
