from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=180, null=True, blank=False)

    def __str__(self):
        return self.name


class carType(models.Model):
    carTypeName = models.CharField(max_length=180, null=True, blank=False)
    desc = models.TextField(null=True, blank=False)

    def __str__(self):
        return self.carTypeName


class mstCar(models.Model):
    carType = models.ForeignKey("carType")
    modelId = models.BigIntegerField(null=True, blank=True)
    ownerId = models.BigIntegerField(null=True, blank=True)
    rentTypeFlag = models.BooleanField(blank=True, default=True)
    rentValue = models.BigIntegerField(null=True, blank=True)


class carRoute(models.Model):
    route = models.BigIntegerField(null=True, blank=True)
    car = models.BigIntegerField(null=True, blank=True)


class mstRoute(models.Model):
    source = models.BigIntegerField(null=True, blank=True)
    destination = models.BigIntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)


class model(models.Model):
    modelName = models.CharField(max_length=180, null=True, blank=False)
    modelId = models.BigIntegerField(null=True, blank=True)
    manufactureId = models.BigIntegerField(null=True, blank=True)


class manufacturer(models.Model):
    manufacturerName = models.CharField(max_length=180, null=True, blank=False)


class mstRegistration(models.Model):
    registeredUserId = models.BigIntegerField(null=True, blank=True)
    registeredCarId = models.BigIntegerField(null=True, blank=True)
    registrationStartDate = models.DateTimeField(null=True, blank=True)
    registrationEndDate = models.DateTimeField(null=True, blank=True)
    registrationStatusId = models.BigIntegerField(null=True, blank=True)








