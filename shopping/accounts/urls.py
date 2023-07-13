from django.urls import path

from .views import loginView, logoutView, registrationView

urlpatterns = [
    path("login/", loginView, name="login"),
    path("logout/", logoutView, name="logout"),
    path("register/", registrationView, name="register"),
]
