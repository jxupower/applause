
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='search-home'),
    path('requirements/', views.requirements, name='search-requirements'),
]

