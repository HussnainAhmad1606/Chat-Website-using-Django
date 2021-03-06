from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = "Pak Chat Admin Login Area"

admin.site.site_title = "Pak Chat cPanel"

admin.site.index_title = "Welcome to Pak Chat cPanel"

urlpatterns = [
    path("", views.home, name="home"),
    path("messages/", views.UserMessages, name="messages"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.handleLogin, name="login"),
    path("logout/", views.logoutUser, name="logout")
]
