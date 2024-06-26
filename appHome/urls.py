from django.urls import path
from . import views

urlpatterns = [
    path('', views.appHome, name="appHome"),
    path('login', views.appLogin, name="appLogin"),
    path('registro', views.appRegister, name="appRegister"),
    path('dashboard', views.appDashboard, name="appDashboard"),
    path('dashboard/medicamentos', views.appDashboardMedicamentos, name="appDashboardMedicamentos"),
    path('dashboard/usuarios', views.appDashboardUsuarios, name="appDashboardUsuarios"),
    path('dashboard/posts', views.appDashboardPosts, name="appDashboardPosts"),
    path('dashboard/integrantes', views.appDashboardIntegrantes, name="appDashboardIntegrantes"),
    path('logout', views.appLogout, name="appLogout"),
    ]
