from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import control

urlpatterns = [
    path('', control.controller),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/', auth_views.LoginView.as_view()),
]