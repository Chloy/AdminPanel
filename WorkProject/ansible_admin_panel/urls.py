from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='ansible_admin_panel_home'),
    path('add_host/', views.add_host, name='ansible_admin_panel_add_host'),
    path('table_detail/<str:slug>/', views.table_detail, name='ansible_admin_panel_table_detail'),
    path('table_detail/<str:slug>/<str:pk>/', views.object_detail, name='ansible_admin_panel_object_detail')
]