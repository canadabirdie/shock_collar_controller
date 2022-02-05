from django.contrib import admin
from django.urls import path

from . import control

urlpatterns = [
    path('shock/', control.controller),
    path('config/', control.config),
]