from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateUserView.as_view(), name="create_user"),
    path("auth/login", views.CustomTokenObtainView.as_view(), name="login")
]
