from django.urls import path

from . import views

urlpatterns = [
    path("", views.ListPropertyView.as_view(), name="list_property"),
]
