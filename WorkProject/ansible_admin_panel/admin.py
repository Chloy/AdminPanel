from jsoneditor.forms import JSONEditor
from django.contrib.admin import widgets
from django.contrib import admin
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

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        kwargs['widget']= widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            db_field.name in self.filter_vertical
        )
        return super(admin.ModelAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)


class HostAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'EQ', 
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
        'vars',
        ]
    list_display = ('EQ', 'name')
    readonly_fields = ['EQ']
    search_fields = ['name', 'EQ']

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        kwargs['widget']= widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            db_field.name in self.filter_vertical
        )
        return super(admin.ModelAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)


class GroupAdmin(admin.ModelAdmin):
    fields = [
        'name',
        'parent',
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
ansible_admin_panel.register(ORG, GroupAdmin)
ansible_admin_panel.register(LOCATION, GroupAdmin)
ansible_admin_panel.register(HV, GroupAdmin)
ansible_admin_panel.register(CLASS, GroupAdmin)
ansible_admin_panel.register(ASSIGNIP, GroupAdmin)
ansible_admin_panel.register(FAMILY, GroupAdmin)
ansible_admin_panel.register(ROLE, GroupAdmin)
ansible_admin_panel.register(FEATURE, GroupAdmin)
ansible_admin_panel.register(TV, GroupAdmin)
ansible_admin_panel.register(KNA, GroupAdmin)
ansible_admin_panel.register(KES, GroupAdmin)
ansible_admin_panel.register(BE, GroupAdmin)
ansible_admin_panel.register(CON, GroupAdmin)
ansible_admin_panel.register(AVAILABILITY, GroupAdmin)
ansible_admin_panel.register(ELK, GroupAdmin)
ansible_admin_panel.register(DINET, GroupAdmin)
ansible_admin_panel.register(WU, GroupAdmin)
ansible_admin_panel.register(SSH, GroupAdmin)
ansible_admin_panel.register(LOCAL_OS, GroupAdmin)
ansible_admin_panel.register(STAGE, GroupAdmin)
ansible_admin_panel.register(VarType)
ansible_admin_panel.register(Var, VarAdmin)