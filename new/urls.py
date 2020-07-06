from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("options",views.options,name="options"),
    path("arthamatic",views.arthamatic,name="arthamatic"),
    path("panchaka",views.panchaka,name="panchaka"),
    path("H", views.H, name="H"),
]