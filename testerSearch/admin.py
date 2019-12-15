from django.contrib import admin
from .models import Tester, Device, Bug
# Register your models here.


admin.site.register(Tester)
admin.site.register(Device)
admin.site.register(Bug)