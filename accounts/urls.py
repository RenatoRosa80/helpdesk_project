


# accounts/urls.py
from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.user_login, name="login"),
    #FORCE o LogoutView explicitamente
    path("logout/", LogoutView.as_view(next_page='accounts:login'), name="logout"),
    path("register/", views.register, name="register"),
    path("user-management/", views.admin_user_list, name="admin_user_list"),
]
