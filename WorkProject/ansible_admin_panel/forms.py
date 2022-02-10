from django import forms
from .models import *

class HostForm(forms.Form):
    name = forms.CharField(max_length=250)
    org = forms.ModelChoiceField(queryset=ORG.objects.all(), label='ORG')
    location = forms.ModelChoiceField(queryset=LOCATION.objects.all(), label='LOCATION')
    hv = forms.ModelChoiceField(queryset=HV.objects.all(), label='HV')
    _class = forms.ModelChoiceField(queryset=CLASS.objects.all(), label='CLASS')
    assignip = forms.ModelChoiceField(queryset=ASSIGNIP.objects.all(), label='ASSIGNIP')
    family = forms.ModelChoiceField(queryset=FAMILY.objects.all(), label='FAMILY')
    role = forms.ModelMultipleChoiceField(queryset=ROLE.objects.all(), label='ROLE')
    features = forms.ModelMultipleChoiceField(queryset=FEATURES.objects.all(), label='FEATURES')
    kna = forms.ModelChoiceField(queryset=KNA.objects.all(), label='KNA')
    kes = forms.ModelChoiceField(queryset=KES.objects.all(), label='KES')
    be = forms.ModelChoiceField(queryset=BE.objects.all(), label='BE')
    con = forms.ModelChoiceField(queryset=CON.objects.all(), label='CON')
    availability = forms.ModelChoiceField(queryset=AVAILABILITY.objects.all(), label='AVAILABILITY')
    elk = forms.ModelChoiceField(queryset=ELK.objects.all(), label='ELK')
    dinet = forms.ModelChoiceField(queryset=DINET.objects.all(), label='DINET')
    wu = forms.ModelChoiceField(queryset=WU.objects.all(), label='WU')
    ssh = forms.ModelChoiceField(queryset=SSH.objects.all(), label='SSH')
    local_os = forms.ModelChoiceField(queryset=LOCAL_OS.objects.all(), label='LOCAL OS')
    stage = forms.ModelChoiceField(queryset=STAGE.objects.all(), label='STAGE')
    #vars = forms.ModelMultipleChoiceField(queryset=Var.objects.all())

    def save(self):
        new_host = Host.objects.create(
            name = self.cleaned_data['name'],
            org = self.cleaned_data['org'],
            location = self.cleaned_data['location'],
            hv = self.cleaned_data['hv'],
            _class = self.cleaned_data['_class'],
            assignip = self.cleaned_data['assignip'],
            family = self.cleaned_data['family'],
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
        new_host.role.add(*self.cleaned_data['role'])
        new_host.features.add(*self.cleaned_data['features'])
        return new_host