from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'testerSearch/home.html')


def requirements(request):
    return render(request, 'testerSearch/requirements.html')





