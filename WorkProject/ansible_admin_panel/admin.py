from jsoneditor.forms import JSONEditor
from django.contrib.admin import widgets
from django.contrib import admin
from django.db import models
from .models import *

class AnsibleAdminPanel(admin.AdminSite):
    site_header = 'Ansible Admin Panel'

ansible_admin_panel = AnsibleAdminPanel(name='AnsibleAdmin')


class VarAdmin(admin.ModelAdmin):
    fields = [
        'var_type',
        'value',
        'json_value'
    ]
    formfield_overrides = {
        models.JSONField:{ 'widget': JSONEditor },
    }

    # def formfield_for_dbfield(self, db_field, request, **kwargs):
    #     field = super().formfield_for_dbfield(db_field, request, **kwargs)
    #     if isinstance(field, forms.fields.JSONField):
    #         field.widget = JSONEditor({
    #             "type": "array",
    #             "items": {
    #                 "type": "string"
    #             }
    #         })
    #     return field


class HostAdmin(admin.ModelAdmin):
    fields = [
        'name', 
        'org', 
        'location', 
        'hv', 
        '_class',
        'assignip', 
        'family', 
        'roles', 
        'features',
        'tv',
        'kna', 
        'kes', 
        'be', 
        'con', 
        'availability', 
        'elk', 
        'dinet',
        'wu',
        'ssh',
        'local_os',
        'stage',
        'vars'
        ]

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        kwargs['widget']= widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            db_field.name in self.filter_vertical
        )
        return super(admin.ModelAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)


ansible_admin_panel.register(Host, HostAdmin)
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
ansible_admin_panel.register(Var, VarAdmin)