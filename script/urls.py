from django.contrib import admin
from django.urls import path, include

from .views import home, pacientes

urlpatterns = [
    path("", home, name="home"),
    path("pacientes/", pacientes, name="pacientes")
]