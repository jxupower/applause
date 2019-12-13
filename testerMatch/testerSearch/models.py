from django.db import models
from django.utils import timezone

# Create your models here.
class Tester(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    country = models.CharField(max_length=10)
    lastLogin = models.DateTimeField(default=timezone.now)

class Device(models.Model):
    deviceName = models.CharField(max_length=20)
    tester = models.ForeignKey(Tester, on_delete=models.CASCADE)


class Bug(models.Model):
    device = models.ManyToManyField(Device)
    tester = models.ForeignKey(Tester, on_delete=models.CASCADE)





    