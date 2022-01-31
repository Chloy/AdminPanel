from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_name, name='ansible_admin_panel_home')
]