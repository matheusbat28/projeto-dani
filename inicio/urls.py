from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout', views.logout, name="logout"),
    path('categoria', views.categoria, name="categoria"),
    path('carrinho', views.carrinho, name="carrinho"),
]