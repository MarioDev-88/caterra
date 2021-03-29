from django.urls import path

from .views import login_view, logout_view, signup_view

app_name = "users"

urlpatterns = [
    path("login/", login_view, name="login_view"),
    path("logout/", logout_view, name="logout_view"),
    path("signup/", signup_view, name="signup_view"),
]
