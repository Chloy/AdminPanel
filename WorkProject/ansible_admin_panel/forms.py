from django import forms
from .models import ORG, Host


class NameForm(forms.Form):
    your_name = forms.ModelChoiceField(queryset=ORG.objects.all())

class HostForm(forms.Form):
    name = forms.CharField(max_length=250)
    org = forms.ModelChoiceField(queryset=ORG.objects.all())

    def save(self):
        new_host = Host.objects.create(
            name = self.cleaned_data['name'],
            org = self.cleaned_data['org']
        )
        return new_host