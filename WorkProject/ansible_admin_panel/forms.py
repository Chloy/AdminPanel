from django import forms
from .models import *

class HostForm(forms.Form):
    name = forms.CharField(max_length=250)
    org = forms.ModelChoiceField(queryset=ORG.objects.all())
    location = forms.ModelChoiceField(queryset=LOCATION.objects.all())
    hv = forms.ModelChoiceField(queryset=HV.objects.all())
    _class = forms.ModelChoiceField(queryset=CLASS.objects.all())
    assignip = forms.ModelChoiceField(queryset=ASSIGNIP.objects.all())
    family = forms.ModelChoiceField(queryset=FAMILY.objects.all())
    role = forms.ModelMultipleChoiceField(queryset=ROLE.objects.all())
    features = forms.ModelMultipleChoiceField(queryset=FEATURES.objects.all())
    kna = forms.ModelChoiceField(queryset=KNA.objects.all())
    kes = forms.ModelChoiceField(queryset=KES.objects.all())
    be = forms.ModelChoiceField(queryset=BE.objects.all())
    con = forms.ModelChoiceField(queryset=CON.objects.all())
    availability = forms.ModelChoiceField(queryset=AVAILABILITY.objects.all())
    elk = forms.ModelChoiceField(queryset=ELK.objects.all())
    dinet = forms.ModelChoiceField(queryset=DINET.objects.all())
    wu = forms.ModelChoiceField(queryset=WU.objects.all())
    ssh = forms.ModelChoiceField(queryset=SSH.objects.all())
    local_os = forms.ModelChoiceField(queryset=LOCAL_OS.objects.all())
    stage = forms.ModelChoiceField(queryset=STAGE.objects.all())
    vars = forms.ModelMultipleChoiceField(queryset=Var.objects.all())

    def save(self):
        print(self.cleaned_data)
        new_host = Host.objects.create(
            name = self.cleaned_data['name'],
            org = self.cleaned_data['org'],
            location = self.cleaned_data['location'],
            hv = self.cleaned_data['hv'],
            clas = self.cleaned_data['clas'],
            assignip = self.cleaned_data['assignip'],
            family = self.cleaned_data['family'],
            role = [r for r in self.cleaned_data['role']],
            features = [f for f in self.cleaned_data['features']],
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
            stage = self.cleaned_data['stage'],
            vars = [v for v in self.cleaned_data['vars']]
        )
        return new_host