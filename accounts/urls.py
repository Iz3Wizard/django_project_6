from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import HomePageview

urlpatterns = [
    path("accounts/login/", auth_views.LoginView.as_view(), name="login",),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout",),
    path("", HomePageview.as_view(), name = "home"),
]