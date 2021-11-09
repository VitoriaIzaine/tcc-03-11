from django.urls import path
from . import views


urlpatterns =[
    path('', views.dashboard, name='dashboard'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('curriculo/', views.curriculo, name='curriculo'),
    path('vagas_aberta/', views.vagas_aberta, name='vagas_aberta'),
    path('vagas_favoritas/', views.vagas_favoritas, name='vagas_favoritas'),

]