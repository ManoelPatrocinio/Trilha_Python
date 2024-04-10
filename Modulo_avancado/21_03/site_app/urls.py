
# from django.contrib import admin
from django.urls import path
from site_app import views

urlpatterns = [
    
    path('', views.home,name="home"),
    path('roupas', views.page_roupas, name='roupas'),
    path('roupa/<produto_id>', views.page_roupa_detalhe, name='roupa_detalhe'),
    
    
    
]
