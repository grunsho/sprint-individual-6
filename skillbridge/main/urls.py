from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('usuarios/', views.UsuariosView.as_view(), name='usuarios'),
    path('registro_usuarios/', views.RegistroUsuariosView.as_view(), name='registro_usuarios'),
    path('registro_usuarios_staff/', views.RegistroUsuarioStaffView.as_view(), name='registro_usuarios_staff'),
    path('index_privado', views.PrivateIndexView.as_view(), name='index_privado'),
    path('accounts/login/', admin.site.urls)
]