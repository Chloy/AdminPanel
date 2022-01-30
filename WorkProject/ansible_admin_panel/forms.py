from hashlib import new
from django import forms
import models

class HostForm(forms.Form):
    name = forms.CharField(max_length=250)
    org = forms.ModelChoiceField(queryset=models.ORG.objects.all())

    def save(self):
        new_host = models.Host.objects.create(
            name = self.name,
            org = self.org
        )
        return new_host