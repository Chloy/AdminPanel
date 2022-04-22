from jsoneditor.forms import JSONEditor
from django.contrib.admin import widgets
from django.contrib import admin
from .models import *


class AnsibleAdminPanel(admin.AdminSite):
    site_header = 'Ansible Admin Panel'
ansible_admin_panel = AnsibleAdminPanel(name='AnsibleAdmin')


class CommonCustomization(admin.ModelAdmin):
    save_on_top = True
    list_per_page = 100
    search_fields = ['name']

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        kwargs['widget']= widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            db_field.name in self.filter_vertical
        )
        return super(admin.ModelAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)


class HostAdmin(CommonCustomization):
    groups = [
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
    ]
    fields = [
        'name',
        'FQDN',
        'EQ',
        *groups,
        'vars'
    ]
    list_display = ('EQ', 'name', 'FQDN')
    list_display_links = ('name',)
    readonly_fields = ['EQ']
    search_fields = ['name', 'FQDN', 'EQ', 'vars__var_type__name', 'vars__value', 'vars__json_value']
    list_filter = [*groups]
    ordering = ['-EQ']


class VarAdmin(CommonCustomization):
    fields = [
        'var_type',
        'value',
        'json_value'
    ]
    formfield_overrides = {
        models.JSONField:{ 'widget': JSONEditor },
    }
    search_fields = [
        'var_type__name',
        'value',
        'json_value'
    ]


class GroupAdmin(CommonCustomization):
    fields = [
        'name',
        'parent',
        'vars'
    ]


mixins = [
    [ORG, GroupAdmin],
    [LOCATION, GroupAdmin],
    [HV, GroupAdmin],
    [CLASS, GroupAdmin],
    [ASSIGNIP, GroupAdmin],
    [FAMILY, GroupAdmin],
    [ROLE, GroupAdmin],
    [FEATURE, GroupAdmin],
    [TV, GroupAdmin],
    [KNA, GroupAdmin],
    [KES, GroupAdmin],
    [BE, GroupAdmin],
    [CON, GroupAdmin],
    [AVAILABILITY, GroupAdmin],
    [ELK, GroupAdmin],
    [DINET, GroupAdmin],
    [WU, GroupAdmin],
    [SSH, GroupAdmin],
    [LOCAL_OS, GroupAdmin],
    [STAGE, GroupAdmin],
    [Host, HostAdmin],
    [VarType, CommonCustomization],
    [Var, VarAdmin]
]

for mix in mixins:
    ansible_admin_panel.register(*mix)
