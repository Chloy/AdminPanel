from django.db import models
from django.shortcuts import reverse

class ORG(models.Model):
    name = models.CharField(unique=True, max_length=250)
    
    def __str__(self):
        return self.name

class LOCATION(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name    

class HV(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class CLASS(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class ASSIGNIP(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class FAMILY(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class ROLE(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class FEATURE(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class TV(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class KNA(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class KES(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class BE(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class CON(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class AVAILABILITY(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class ELK(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class DINET(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class WU(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class SSH(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class LOCAL_OS(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class STAGE(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class VarType(models.Model):
    name = models.CharField(unique=True, max_length=250)

    def __str__(self):
        return self.name

class Var(models.Model):
    var_type = models.ForeignKey(VarType, on_delete=models.CASCADE)
    value = models.CharField(max_length=250)

    def __str__(self):
        return "{}={}".format(self.var_type, self.value)

class Host(models.Model):
    name = models.CharField(unique=True, max_length=250)
    org = models.ForeignKey(ORG, on_delete=models.DO_NOTHING)
    location = models.ForeignKey(LOCATION, on_delete=models.DO_NOTHING)
    hv = models.ForeignKey(HV, on_delete=models.DO_NOTHING)
    _class = models.ForeignKey(CLASS, on_delete=models.DO_NOTHING)
    assignip = models.ForeignKey(ASSIGNIP, on_delete=models.DO_NOTHING, limit_choices_to={'name__startswith': 'a-'})
    family = models.ForeignKey(FAMILY, on_delete=models.DO_NOTHING)
    roles = models.ManyToManyField(ROLE, blank=True)
    features = models.ManyToManyField(FEATURE, blank=True)
    kna = models.ForeignKey(KNA, on_delete=models.DO_NOTHING)
    kes = models.ForeignKey(KES, on_delete=models.DO_NOTHING)
    be = models.ForeignKey(BE, on_delete=models.DO_NOTHING)
    con = models.ForeignKey(CON, on_delete=models.DO_NOTHING)
    availability = models.ForeignKey(AVAILABILITY, on_delete=models.DO_NOTHING)
    elk = models.ForeignKey(ELK, on_delete=models.DO_NOTHING)
    dinet = models.ForeignKey(DINET, on_delete=models.DO_NOTHING)
    wu = models.ForeignKey(WU, on_delete=models.DO_NOTHING)
    ssh = models.ForeignKey(SSH, on_delete=models.DO_NOTHING)
    local_os = models.ForeignKey(LOCAL_OS, on_delete=models.DO_NOTHING)
    stage = models.ForeignKey(STAGE, on_delete=models.DO_NOTHING)
    vars = models.ManyToManyField(Var, blank=True)

    def get_absolute_url(self):
        return reverse('ansible_admin_panel_object_detail', kwargs={'slug': 'host', 'pk': self.pk})

    def __str__(self):
        return self.name