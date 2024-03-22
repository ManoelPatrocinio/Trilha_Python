
# from django.contrib import admin
from django.urls import path
from site_app import views

urlpatterns = [
    
    path('', views.home,name="home"),
    path('roupas', views.page_prod_detail, name='roupas'),
    path('detalhes', views.page_prod_detail, name='detalhes_produto')
]
