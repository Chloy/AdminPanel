from importlib.metadata import requires
from urllib import request
from django.db import models

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

class FEATURES(models.Model):
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

# class Host(models.Model):
#     name = models.CharField(unique=True, max_length=250)
#     org = models.ForeignKey(ORG, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     location = models.ForeignKey(LOCATION, on_delete=models.DO_NOTHING, default=LOCATION.objects.get(name='DEF'))
#     hv = models.ForeignKey(HV, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     clas = models.ForeignKey(CLASS, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     assignip = models.ForeignKey(ASSIGNIP, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     family = models.ForeignKey(FAMILY, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     role = models.ForeignKey(ROLE, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     features = models.ForeignKey(FEATURES, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     kna = models.ForeignKey(KNA, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     kes = models.ForeignKey(KES, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     be = models.ForeignKey(BE, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     con = models.ForeignKey(CON, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     availability = models.ForeignKey(AVAILABILITY, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     elk = models.ForeignKey(ELK, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     dinet = models.ForeignKey(DINET, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     wu = models.ForeignKey(WU, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     ssh = models.ForeignKey(SSH, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
#     local_os = models.ForeignKey(LOCAL_OS, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))
# #     stage = models.ForeignKey(STAGE, on_delete=models.DO_NOTHING, default=ORG.objects.get(name='DEF'))

#     def __str__(self):
#         return self.name