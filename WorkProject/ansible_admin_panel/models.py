from django.db import models
from django.db.models import Max
from yamlfield.fields import YAMLField


class GroupCommon(models.Model):
    name = models.CharField(unique=True, max_length=100)
    parent = models.ForeignKey("self", blank=True, on_delete=models.SET_NULL, null=True)
    vars = models.ManyToManyField('Var', blank=True)

    class Meta():
        abstract = True
    
    def __str__(self):
        return self.name


class VarType(models.Model):
    name = models.CharField(unique=True, max_length=250)

    class Meta:
        verbose_name_plural = "Var type"

    def __str__(self):
        return self.name
    
    
class Var(models.Model):
    var_type = models.ForeignKey(VarType, on_delete=models.CASCADE)
    value = YAMLField()

    class Meta:
        verbose_name_plural = "Var"

    def __str__(self):
        return "{}={}".format(self.var_type, self.value)


class ORG(GroupCommon):
    class Meta():
        verbose_name_plural = "ORG"    


class LOCATION(GroupCommon):
    class Meta:
        verbose_name_plural = "LOCATION"
    
    
class HV(GroupCommon):
    class Meta:
        verbose_name_plural = "HV"


class CLASS(GroupCommon):
    class Meta:
        verbose_name_plural = "CLASS"


class ASSIGNIP(GroupCommon):
    class Meta:
        verbose_name_plural = "ASSIGNIP"

 
class FAMILY(GroupCommon):
    class Meta:
        verbose_name_plural = "FAMILY"

    
class ROLE(GroupCommon):
    class Meta:
        verbose_name_plural = "ROLE"


class FEATURE(GroupCommon):
    class Meta:
        verbose_name_plural = "FEATURE"

    
class TV(GroupCommon):
    class Meta:
        verbose_name_plural = "TV"


class KNA(GroupCommon):
    class Meta:
        verbose_name_plural = "KNA"

    
class KES(GroupCommon):
    class Meta:
        verbose_name_plural = "KES"


class BE(GroupCommon):
    class Meta:
        verbose_name_plural = "BE"

 
class CON(GroupCommon):
    class Meta:
        verbose_name_plural = "CON"

    
class AVAILABILITY(GroupCommon):
    class Meta:
        verbose_name_plural = "AVAILABILITY"

    
class ELK(GroupCommon):
    class Meta:
        verbose_name_plural = "ELK"

    
class DINET(GroupCommon):
    class Meta:
        verbose_name_plural = "DINET"

    
class WU(GroupCommon):
    class Meta:
        verbose_name_plural = "WU"


class SSH(GroupCommon):
    class Meta:
        verbose_name_plural = "SSH"

 
class LOCAL_OS(GroupCommon):
    class Meta:
        verbose_name_plural = "LOCAL OS"


class STAGE(GroupCommon):
    class Meta:
        verbose_name_plural = "STAGE"


class Host(models.Model):
    name = models.CharField(max_length=250)
    FQDN = models.CharField(max_length=250)
    org = models.ForeignKey(ORG, on_delete=models.DO_NOTHING, default=ORG.objects.get_or_create(name='UNKNOWN')[0].id)
    location = models.ForeignKey(LOCATION, on_delete=models.DO_NOTHING, default=LOCATION.objects.get_or_create(name='UNKNOWN')[0].id)
    hv = models.ForeignKey(HV, on_delete=models.DO_NOTHING, default=HV.objects.get_or_create(name='UNKNOWN')[0].id)
    _class = models.ForeignKey(CLASS, on_delete=models.DO_NOTHING, default=CLASS.objects.get_or_create(name='UNKNOWN')[0].id)
    assignip = models.ForeignKey(ASSIGNIP, on_delete=models.DO_NOTHING, default=ASSIGNIP.objects.get_or_create(name='UNKNOWN')[0].id)
    family = models.ForeignKey(FAMILY, on_delete=models.DO_NOTHING, default=FAMILY.objects.get_or_create(name='UNKNOWN')[0].id)
    roles = models.ManyToManyField(ROLE, blank=False)
    features = models.ManyToManyField(FEATURE, blank=False)
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

    class Meta:
        verbose_name_plural = "Host"

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.EQ == None:
            max = Host.objects.aggregate(Max('EQ'))['EQ__max']
            if max is None: max = 0
            self.EQ = max + 1
        super(Host, self).save(*args, **kwargs)