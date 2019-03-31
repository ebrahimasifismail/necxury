from django.contrib import admin
from django.urls import path
from design import views



urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
]