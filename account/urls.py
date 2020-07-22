from django.urls import path
from . import views

urlpatterns = [
    path("/register", views.register, name="register"),
    path("/logout", views.logout, name="logout"),
    path("/dashboard", views.dashboard, name="dashboard"),
    path("/login/", views.login, name="login"),
]
