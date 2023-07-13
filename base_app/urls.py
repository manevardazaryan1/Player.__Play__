from django.urls import path

from base_app import views


app_name = "base_app"

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about", views.AboutView.as_view(), name="about"),
]