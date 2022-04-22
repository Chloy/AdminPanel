from django.urls import path
from . import views, admin

urlpatterns = [
    path('admin/', admin.ansible_admin_panel.urls),
]