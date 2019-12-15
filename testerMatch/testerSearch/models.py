from django.db import models
from django.utils import timezone

# Create your models here.
class Tester(models.Model):
    firstName = models.CharField(max_length=40)
    lastName = models.CharField(max_length=40)
    country = models.CharField(max_length=10)
    lastLogin = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.firstName} {self.lastName}' 

class Device(models.Model):
    deviceName = models.CharField(max_length=20)
    tester = models.ManyToManyField(Tester)

    def __str__(self):
        return f'{self.deviceName}'

class Bug(models.Model):
    device = models.ForeignKey(Device, default=0, on_delete=models.CASCADE)
    tester = models.ForeignKey(Tester, default=0, on_delete=models.CASCADE)





    