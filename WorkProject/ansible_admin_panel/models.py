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

class Host(models.Model):
    name = models.CharField(unique=True, max_length=250)
    org = models.ForeignKey(ORG, on_delete=models.DO_NOTHING)