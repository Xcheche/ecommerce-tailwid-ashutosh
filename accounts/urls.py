
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from accounts.decorators import redirect_authenticated_user


urlpatterns = [
    path("register/", views.register, name="register"),
    path("logout/", views.logout_view, name="logout"),
    
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html", redirect_authenticated_user=True), name="login"),
    path("profile/", views.profile, name="profile"),
]