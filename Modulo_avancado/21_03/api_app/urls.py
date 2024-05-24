
# from django.contrib import admin
from django.urls import path
from api_app import views

urlpatterns = [
    path('get-roupas', views.roupas),
      
]
 