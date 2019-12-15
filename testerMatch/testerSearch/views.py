from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Tester, Device, Bug


# Create your views here.

def home(request):
    exp = filter(request)
    country = request.GET.get('countries')
    device = request.GET.get('devices')
    devices = Device.objects.all()
    countries = []
    for t in Tester.objects.all():
        if t.country not in countries:
            countries.append(t.country)
    context = {
        'experience': sorted(exp.items(),key=lambda x: x[1],reverse=True),
        'countries': countries,
        'devices': devices,
        'deviceSelected': device,
        'countrySelected': country
    }
    return render(request, 'testerSearch/home.html', context)


def requirements(request):
    return render(request, 'testerSearch/requirements.html')



def filter(request):
    country = request.GET.get('countries')
    device = request.GET.get('devices')
    qs = Tester.objects.all()
    if country != "ALL":
        qs = qs.filter(country=country)
    if device != "ALL":
        qs = qs.filter(device__tester=Device.objects.get(deviceName=device).id)
    exp = {}
    for tester in qs:
        bugs = Bug.objects.all()
        bugs = bugs.filter(tester=tester.id)
        exp[tester] = bugs.count()
    return exp
