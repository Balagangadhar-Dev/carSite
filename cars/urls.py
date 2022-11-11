from django.urls import path

from . import views

app_name='cars'


urlpatterns = [
    path('', views.index, name='index'),
    path('admin1/', views.admin1, name='admin1'),
]