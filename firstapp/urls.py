from django.urls import path
from . import views

urlpatterns = [
    path('', views.name, name="name"),
    path('name', views.home, name="home"),
    path('add', views.add, name="add")]
