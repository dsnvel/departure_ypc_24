from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile_detail, name='profile'),
    path('task-manger/', views.registration_view, name='task-manger'),
    # Нужно обработать пути по функционалу, например, когда мы что-то передаем
]
