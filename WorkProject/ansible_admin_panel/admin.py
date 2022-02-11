from django.contrib import admin
from .models import *

class AnsibleAdminPanel(admin.AdminSite):
    site_header = 'Ansible Admin Panel'

ansible_admin_panel = AnsibleAdminPanel(name='AnsibleAdmin')

ansible_admin_panel.register(Host)
ansible_admin_panel.register(ORG)
ansible_admin_panel.register(LOCATION)
ansible_admin_panel.register(HV)
ansible_admin_panel.register(CLASS)
ansible_admin_panel.register(ASSIGNIP)
ansible_admin_panel.register(FAMILY)
ansible_admin_panel.register(ROLE)
ansible_admin_panel.register(FEATURE)
ansible_admin_panel.register(TV)
ansible_admin_panel.register(KNA)
ansible_admin_panel.register(KES)
ansible_admin_panel.register(BE)
ansible_admin_panel.register(CON)
ansible_admin_panel.register(AVAILABILITY)
ansible_admin_panel.register(ELK)
ansible_admin_panel.register(DINET)
ansible_admin_panel.register(WU)
ansible_admin_panel.register(SSH)
ansible_admin_panel.register(LOCAL_OS)
ansible_admin_panel.register(STAGE)
ansible_admin_panel.register(VarType)
ansible_admin_panel.register(Var)