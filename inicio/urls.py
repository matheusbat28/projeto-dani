from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('logout', views.logout, name="logout"),
    path('categoria', views.categoria, name="categoria"),
    path('produtos', views.produtos, name="produtos"),
    path('carrinho', views.carrinho, name="carrinho"),
    path('deletarCart/<int:id>/', views.deletarCart, name='deletarCart'),
    path('perfil/', views.perfil, name='perfil'),
    path('buscar/', views.buscar, name='buscar'),
]