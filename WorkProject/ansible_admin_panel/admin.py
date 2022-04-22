from jsoneditor.forms import JSONEditor
from django.contrib.admin import widgets
from django.contrib import admin
from .models import *
from django.urls import reverse


class AnsibleAdminPanel(admin.AdminSite):
    site_header = 'Ansible Admin Panel'
ansible_admin_panel = AnsibleAdminPanel(name='AnsibleAdmin')


class ManyToMany(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        kwargs['widget']= widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            db_field.name in self.filter_vertical
        )
        return super(admin.ModelAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)


class HostAdmin(ManyToMany, admin.ModelAdmin):
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
    # fieldsets = (
    #     (None, {
    #         'fields': [
    #             'name',
    #             'EQ', 
    #             ]
    #     }),
    #     ('Advanced', {
    #         'classes': ('wide', 'extrapretty'),
    #         'fields': [
    #             *groups,
    #             'vars'
    #         ]
    #     })
    # )
    list_display = ('EQ', 'name', 'FQDN')
    list_display_links = ('name',)
    readonly_fields = ['EQ']
    save_on_top = True
    list_per_page = 100
    search_fields = ['name', 'FQDN', 'EQ', 'vars__var_type__name', 'vars__value', 'vars__json_value']
    list_filter = [*groups]
    ordering = ['-EQ']


class VarAdmin(ManyToMany, admin.ModelAdmin):
    fields = [
        'var_type',
        'value',
        'json_value'
    ]
    formfield_overrides = {
        models.JSONField:{ 'widget': JSONEditor },
    }


class GroupAdmin(ManyToMany, admin.ModelAdmin):
    fields = [
        'name',
        'parent',
        'vars'
    ]

mixins = [
    [Host, HostAdmin],
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
    [VarType],
    [Var, VarAdmin]
]

for mix in mixins:
    ansible_admin_panel.register(*mix)
