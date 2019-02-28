from django.urls import path

from . import views

urlpatterns = [
    path('damian', views.home, name='home'),
    path('', views.index, name='index'),
]