from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
from django.db import models


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

    def __str__(self):
        return "CarType: " + str(self.carType) + " / ModelId: " + str(self.modelId)


class carRoute(models.Model):
    route = models.BigIntegerField(null=True, blank=True)
    car = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.route)


class mstRoute(models.Model):
    source = models.BigIntegerField(null=True, blank=True)
    destination = models.BigIntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "Source: " + str(self.source) + " / Destination: " + str(self.destination)


class carModel(models.Model):
    modelName = models.CharField(max_length=180, null=True, blank=False)
    manufacturer = models.ForeignKey("manufacturer", null=True, blank=True)

    def __str__(self):
        return "Model Name: " + str(self.modelName) + " / ModelId: " + str(self.id)


class manufacturer(models.Model):
    manufacturerName = models.CharField(max_length=180, null=True, blank=False)

    def __str__(self):
        return str(self.manufacturerName)


class mstRegistration(models.Model):
    registeredUserId = models.BigIntegerField(null=True, blank=True)
    registeredCarId = models.BigIntegerField(null=True, blank=True)
    registrationStartDate = models.DateTimeField(null=True, blank=True)
    registrationEndDate = models.DateTimeField(null=True, blank=True)
    registrationStatusId = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return "UserId: " + str(self.registeredUserId) + " / CarId: " + str(self.registeredCarId)


class manufacturerRegistration(models.Model):
    license_number = models.CharField(max_length=256, null=True, blank=False)
    manufacturing_date = models.DateTimeField(null=True, blank=False)
    manufacturer = models.ForeignKey("manufacturer", null=True, blank=True)
    model = models.ForeignKey(carModel, null=True, blank=False)
    fuel_type = models.ForeignKey("fuelType", null=True, blank=True)
    vehicle_color = models.ForeignKey("vehicleColour", null=True, blank=False)
    vehicle_type = models.ForeignKey(carType, null=True, blank=False)
    km_run = models.CharField(max_length=256, null=True, blank=False)
    rc = models.FileField(null=True, blank=True)
    fitness = models.FileField(null=True, blank=True)
    permit = models.FileField(null=True, blank=True)
    insurance = models.FileField(null=True, blank=True)
    pollution = models.FileField(null=True, blank=True)
    rateList = models.ForeignKey("rateList", null=True, blank=True)

    def __str__(self):
        return "License No: " + str(self.license_number) + " / Manufacturer: " + str(self.manufacturer) + "/ KM " \
                                                                                                               "Run:" \
               + str(self.km_run)


class ownerRegistration(models.Model):
    name = models.CharField(max_length=256, null=True, blank=False)
    mobileNumber = models.BigIntegerField(null=True, blank=False)
    licenseNumber = models.CharField(max_length=256, null=True, blank=False)
    dateOfBirth = models.DateField(null=True, blank=False)
    aadharCardFront = models.FileField(null=True, blank=True)
    aadharCardBack = models.FileField(null=True, blank=True)
    licenseFront = models.FileField(null=True, blank=True)
    licenseBack = models.FileField(null=True, blank=True)
    photo = models.FileField(null=True, blank=True)
    addressProof = models.FileField(null=True, blank=True)
    normsAccepted = models.BooleanField(default=True)
    manufacturer = models.ForeignKey("manufacturerRegistration", null=True, blank=True)

    def __str__(self):
        return "License No: " + str(self.licenseNumber) + " / Driver: " + str(self.name)


class rateList(models.Model):
    rate = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return "Rate: " + str(self.rate)


class fuelType(models.Model):
    type = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "FuelType: " + str(self.type)


class vehicleColour(models.Model):
    colour = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return "VehicleColour: " + str(self.colour)

