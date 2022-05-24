from operator import attrgetter
from jsoneditor.forms import JSONEditor
from django.contrib.admin import widgets
from django.contrib import admin
from .models import *
from itertools import chain


class AnsibleAdminPanel(admin.AdminSite):
    site_header = 'Ansible Admin Panel'
ansible_admin_panel = AnsibleAdminPanel(name='AnsibleAdmin')


class CommonCustomization(admin.ModelAdmin):
    list_per_page = 100
    search_fields = ['name']

    def formfield_for_foreignkey(self, db_field, request=None, **kwargs):
        print(db_field.name)
        fields = {
            'org': ORG.objects.exclude(name='org'),
            'location': LOCATION.objects.exclude(name='loc'),
            'hv': HV.objects.exclude(name='t'),
            '_class': CLASS.objects.exclude(name='c'),
            'assignip': ASSIGNIP.objects.exclude(name='a'),
            'family': FAMILY.objects.exclude(name='f'),
            'tv': TV.objects.exclude(name='tv'),
            'kna': KNA.objects.exclude(name='kna'),
            'kes': KES.objects.exclude(name='kes'),
            'be': BE.objects.exclude(name='be'),
            'con': CON.objects.exclude(name='con'),
            'availability': AVAILABILITY.objects.exclude(name='avail'),
            'elk': ELK.objects.exclude(name='elk'),
            'dinet': DINET.objects.exclude(name='di'),
            'wu': WU.objects.exclude(name='wu'),
            'ssh': SSH.objects.exclude(name='ssh'),
            'local_os': LOCAL_OS.objects.exclude(name='lo'),
            'stage': STAGE.objects.exclude(name='st')
        }
        if db_field.model == Host:
            try:
                kwargs['queryset'] = fields[db_field.name]
            except KeyError:
                pass
        return super(admin.ModelAdmin, self).formfield_for_foreignkey(
            db_field, request=request, **kwargs)

    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        kwargs['widget']= widgets.FilteredSelectMultiple(
            db_field.verbose_name,
            db_field.name in self.filter_vertical
        )
        
        fields = {
            'roles': ROLE.objects.exclude(name='role'),
            'features': FEATURE.objects.exclude(name='feat'),
        }
        try:
            kwargs['queryset']=fields[db_field.name]
        except KeyError:
            pass

        return super(admin.ModelAdmin, self).formfield_for_manytomany(
            db_field, request=request, **kwargs)


class HostAdmin(CommonCustomization):
    save_on_top = True
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
        'value'
    ]
    search_fields = [
        'var_type__name',
        'value'
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
