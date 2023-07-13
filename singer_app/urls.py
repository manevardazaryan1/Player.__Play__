from django.urls import path

from singer_app import views


app_name = "singer_app"

urlpatterns = [
    path('singer/', views.SingerView.as_view(), name='singer'),
    path('singer/detail/<slug:slug>/', views.SingerDetailView.as_view(), name='detail'),
]