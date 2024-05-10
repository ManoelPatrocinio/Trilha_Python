from django.urls import path
from taygra_app import views

urlpatterns = [
    
    path('', views.home,name="home"),
    path('login', views.page_login,name="login"),
    path('logout', views.page_logout,name="logout"),
    path('registro', views.page_registro,name="cadastro"),
    
     
]