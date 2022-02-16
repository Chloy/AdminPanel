from dataclasses import field
from django import forms
from .models import *

class HostForm(forms.ModelForm):

    class Meta:
        model = Host
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
            'stage'
            ]

    def save(self):
        new_host = Host.objects.create(
            name = self.cleaned_data['name'],
            org = self.cleaned_data['org'],
            location = self.cleaned_data['location'],
            hv = self.cleaned_data['hv'],
            _class = self.cleaned_data['_class'],
            assignip = self.cleaned_data['assignip'],
            family = self.cleaned_data['family'],
            tv = self.cleaned_data['tv'],
            kna = self.cleaned_data['kna'],
            kes = self.cleaned_data['kes'],
            be = self.cleaned_data['be'],
            con = self.cleaned_data['con'],
            availability = self.cleaned_data['availability'],
            elk = self.cleaned_data['elk'],
            dinet = self.cleaned_data['dinet'],
            wu = self.cleaned_data['wu'],
            ssh = self.cleaned_data['ssh'],
            local_os = self.cleaned_data['local_os'],
            stage = self.cleaned_data['stage']
        )
        new_host.roles.add(*self.cleaned_data['roles'])
        new_host.features.add(*self.cleaned_data['features'])
        return new_host

class ORGForm(forms.ModelForm):
    class Meta:
        model = ORG
        fields = [
            'name'
        ]

    def save(self):
        new_org = ORG.objects.create(
            name = self.cleaned_data('name')
        )
        return new_org

class LOCATIONForm(forms.ModelForm):
    class Meta:
        model = LOCATION
        fields = [
            'name'
        ]

    def save(self):
        new_location = LOCATION.objects.create(
            name = self.cleaned_data('name')
        )
        return new_location

class HVForm(forms.ModelForm):
    class Meta:
        model = HV
        fields = [
            'name'
        ]

    def save(self):
        new_hv = HV.objects.create(
            name = self.cleaned_data('name')
        )
        return new_hv

class CLASSForm(forms.ModelForm):
    class Meta:
        model = CLASS
        fields = [
            'name'
        ]

    def save(self):
        new_class= CLASS.objects.create(
            name = self.cleaned_data('name')
        )
        return new_class

class ASSIGNIPForm(forms.ModelForm):
    class Meta:
        model = ASSIGNIP
        fields = [
            'name'
        ]

    def save(self):
        new_assignip = ASSIGNIP.objects.create(
            name = self.cleaned_data('name')
        )
        return new_assignip

class FAMILYForm(forms.ModelForm):
    class Meta:
        model = FAMILY
        fields = [
            'name'
        ]

    def save(self):
        new_family = FAMILY.objects.create(
            name = self.cleaned_data('name')
        )
        return new_family

class ROLEForm(forms.ModelForm):
    class Meta:
        model = ROLE
        fields = [
            'name'
        ]

    def save(self):
        new_role = ROLE.objects.create(
            name = self.cleaned_data('name')
        )
        return new_role

class FEATUREForm(forms.ModelForm):
    class Meta:
        model = FEATURE
        fields = [
            'name'
        ]

    def save(self):
        new_feature = FEATURE.objects.create(
            name = self.cleaned_data('name')
        )
        return new_feature

class TVForm(forms.ModelForm):
    class Meta:
        model = TV
        fields = [
            'name'
        ]

    def save(self):
        new_tv = TV.objects.create(
            name = self.cleaned_data('name')
        )
        return new_tv

class KNAForm(forms.ModelForm):
    class Meta:
        model = KNA
        fields = [
            'name'
        ]

    def save(self):
        new_kna = KNA.objects.create(
            name = self.cleaned_data('name')
        )
        return new_kna

class KESForm(forms.ModelForm):
    class Meta:
        model = KES
        fields = [
            'name'
        ]

    def save(self):
        new_kes = KES.objects.create(
            name = self.cleaned_data('name')
        )
        return new_kes

class BEForm(forms.ModelForm):
    class Meta:
        model = BE
        fields = [
            'name'
        ]

    def save(self):
        new_be = BE.objects.create(
            name = self.cleaned_data('name')
        )
        return new_be

class CONForm(forms.ModelForm):
    class Meta:
        model = CON
        fields = [
            'name'
        ]

    def save(self):
        new_con = CON.objects.create(
            name = self.cleaned_data('name')
        )
        return new_con

class AVAILABILITYForm(forms.ModelForm):
    class Meta:
        model = AVAILABILITY
        fields = [
            'name'
        ]

    def save(self):
        new_availability = AVAILABILITY.objects.create(
            name = self.cleaned_data('name')
        )
        return new_availability

class ELKForm(forms.ModelForm):
    class Meta:
        model = ELK
        fields = [
            'name'
        ]

    def save(self):
        new_elk = ELK.objects.create(
            name = self.cleaned_data('name')
        )
        return new_elk

class DINETForm(forms.ModelForm):
    class Meta:
        model = DINET
        fields = [
            'name'
        ]

    def save(self):
        new_dinet = DINET.objects.create(
            name = self.cleaned_data('name')
        )
        return new_dinet

class WUForm(forms.ModelForm):
    class Meta:
        model = WU
        fields = [
            'name'
        ]

    def save(self):
        new_wu = WU.objects.create(
            name = self.cleaned_data('name')
        )
        return new_wu

class SSHForm(forms.ModelForm):
    class Meta:
        model = SSH
        fields = [
            'name'
        ]

    def save(self):
        new_ssh = SSH.objects.create(
            name = self.cleaned_data('name')
        )
        return new_ssh

class LOCAL_OSForm(forms.ModelForm):
    class Meta:
        model = LOCAL_OS
        fields = [
            'name'
        ]

    def save(self):
        new_local_os = LOCAL_OS.objects.create(
            name = self.cleaned_data('name')
        )
        return new_local_os

class STAGEForm(forms.ModelForm):
    class Meta:
        model = STAGE
        fields = [
            'name'
        ]

    def save(self):
        new_stage = STAGE.objects.create(
            name = self.cleaned_data('name')
        )
        return new_stage