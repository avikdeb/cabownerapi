from django.utils.encoding import smart_unicode
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=180, null=True, blank=False)

    def __str__(self):
        return self.name
