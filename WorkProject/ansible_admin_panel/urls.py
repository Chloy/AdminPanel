from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ansible_admin_panel_home'),
    path('add_host/', views.add_host, name='ansible_admin_panel_add_host')
]