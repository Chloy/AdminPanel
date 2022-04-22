from django.db import models
from django.db.models import Max

class VarType(models.Model):

    class Meta:
        verbose_name_plural = "Var type"

    name = models.CharField(unique=True, max_length=250)
    
    def __str__(self):
        return self.name

class Var(models.Model):

    class Meta:
        verbose_name_plural = "Var"

    var_type = models.ForeignKey(VarType, on_delete=models.CASCADE)
    value = models.CharField(max_length=250, blank=True, null=True)
    json_value = models.JSONField(null=True, blank=True)

    def __str__(self):
        return "{}={}".format(self.var_type, self.value)

class ORG(models.Model):

    class Meta:
        verbose_name_plural = "ORG"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)
    
    def __str__(self):
        return self.name

class LOCATION(models.Model):

    class Meta:
        verbose_name_plural = "LOCATION"
    
    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name    

class HV(models.Model):

    class Meta:
        verbose_name_plural = "HV"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class CLASS(models.Model):

    class Meta:
        verbose_name_plural = "CLASS"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class ASSIGNIP(models.Model):

    class Meta:
        verbose_name_plural = "ASSIGNIP"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class FAMILY(models.Model):

    class Meta:
        verbose_name_plural = "FAMILY"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class ROLE(models.Model):

    class Meta:
        verbose_name_plural = "ROLE"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class FEATURE(models.Model):

    class Meta:
        verbose_name_plural = "FEATURE"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class TV(models.Model):

    class Meta:
        verbose_name_plural = "TV"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class KNA(models.Model):

    class Meta:
        verbose_name_plural = "KNA"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class KES(models.Model):

    class Meta:
        verbose_name_plural = "KES"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class BE(models.Model):

    class Meta:
        verbose_name_plural = "BE"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class CON(models.Model):

    class Meta:
        verbose_name_plural = "CON"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class AVAILABILITY(models.Model):

    class Meta:
        verbose_name_plural = "AVAILABILITY"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)
    
    def __str__(self):
        return self.name

class ELK(models.Model):

    class Meta:
        verbose_name_plural = "ELK"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class DINET(models.Model):

    class Meta:
        verbose_name_plural = "DINET"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class WU(models.Model):

    class Meta:
        verbose_name_plural = "WU"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name

class SSH(models.Model):

    class Meta:
        verbose_name_plural = "SSH"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)
    
    def __str__(self):
        return self.name

class LOCAL_OS(models.Model):

    class Meta:
        verbose_name_plural = "LOCAL OS"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)


    def __str__(self):
        return self.name

class STAGE(models.Model):

    class Meta:
        verbose_name_plural = "STAGE"

    name = models.CharField(unique=True, max_length=250)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField(Var, blank=True)

    def __str__(self):
        return self.name


class Host(models.Model):

    class Meta:
        verbose_name_plural = "Host"

    name = models.CharField(max_length=250)
    FQDN = models.CharField(max_length=250)
    org = models.ForeignKey(ORG, on_delete=models.DO_NOTHING, default=ORG.objects.get_or_create(name='UNKNOWN')[0].id)
    location = models.ForeignKey(LOCATION, on_delete=models.DO_NOTHING, default=LOCATION.objects.get_or_create(name='UNKNOWN')[0].id)
    hv = models.ForeignKey(HV, on_delete=models.DO_NOTHING, default=HV.objects.get_or_create(name='UNKNOWN')[0].id)
    _class = models.ForeignKey(CLASS, on_delete=models.DO_NOTHING, default=CLASS.objects.get_or_create(name='UNKNOWN')[0].id)
    assignip = models.ForeignKey(ASSIGNIP, on_delete=models.DO_NOTHING, default=ASSIGNIP.objects.get_or_create(name='UNKNOWN')[0].id)
    family = models.ForeignKey(FAMILY, on_delete=models.DO_NOTHING, default=FAMILY.objects.get_or_create(name='UNKNOWN')[0].id)
    roles = models.ManyToManyField(ROLE, blank=True)
    features = models.ManyToManyField(FEATURE, blank=True)
    tv = models.ForeignKey(TV, on_delete=models.DO_NOTHING, default=TV.objects.get_or_create(name='UNKNOWN')[0].id)
    kna = models.ForeignKey(KNA, on_delete=models.DO_NOTHING, default=KNA.objects.get_or_create(name='UNKNOWN')[0].id)
    kes = models.ForeignKey(KES, on_delete=models.DO_NOTHING, default=KES.objects.get_or_create(name='UNKNOWN')[0].id)
    be = models.ForeignKey(BE, on_delete=models.DO_NOTHING, default=BE.objects.get_or_create(name='UNKNOWN')[0].id)
    con = models.ForeignKey(CON, on_delete=models.DO_NOTHING, default=CON.objects.get_or_create(name='UNKNOWN')[0].id)
    availability = models.ForeignKey(AVAILABILITY, on_delete=models.DO_NOTHING, default=AVAILABILITY.objects.get_or_create(name='UNKNOWN')[0].id)
    elk = models.ForeignKey(ELK, on_delete=models.DO_NOTHING, default=ELK.objects.get_or_create(name='UNKNOWN')[0].id)
    dinet = models.ForeignKey(DINET, on_delete=models.DO_NOTHING, default=DINET.objects.get_or_create(name='UNKNOWN')[0].id)
    wu = models.ForeignKey(WU, on_delete=models.DO_NOTHING, default=WU.objects.get_or_create(name='UNKNOWN')[0].id)
    ssh = models.ForeignKey(SSH, on_delete=models.DO_NOTHING, default=SSH.objects.get_or_create(name='UNKNOWN')[0].id)
    local_os = models.ForeignKey(LOCAL_OS, on_delete=models.DO_NOTHING, default=LOCAL_OS.objects.get_or_create(name='UNKNOWN')[0].id)
    stage = models.ForeignKey(STAGE, on_delete=models.DO_NOTHING, default=STAGE.objects.get_or_create(name='UNKNOWN')[0].id)
    vars = models.ManyToManyField(
        Var, 
        blank=True,
        # limit_choices_to={
        #     'var_type_id': VarType.objects.get(name='ansible_host'),
        # }
    )
    EQ = models.IntegerField(unique=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.EQ == None:
            max = Host.objects.aggregate(Max('EQ'))['EQ__max']
            if max is None: max = 0
            self.EQ = max + 1
        super(Host, self).save(*args, **kwargs)