"""gradinite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('gradinite_private/sector1', views.gradinite_private_sector1, name='gradinite_private/sector1'),
    path('gradinite_private/sector2', views.gradinite_private_sector2, name='gradinite_private/sector2'),
    path('gradinite_private/sector3', views.gradinite_private_sector3, name='gradinite_private/sector3'),
    path('gradinite_private/sector4', views.gradinite_private_sector4, name='gradinite_private/sector4'),
    path('gradinite_private/sector5', views.gradinite_private_sector5, name='gradinite_private/sector5'),
    path('gradinite_private/sector6', views.gradinite_private_sector6, name='gradinite_private/sector6'),
    path('gradinite_private/ilfov', views.gradinite_private_ilfov, name='gradinite_private/ilfov'),

    path('gradinite_stat/sector1', views.gradinite_stat_sector1, name='gradinite_stat/sector1'),
    path('gradinite_stat/sector2', views.gradinite_stat_sector2, name='gradinite_stat/sector2'),
    path('gradinite_stat/sector3', views.gradinite_stat_sector3, name='gradinite_stat/sector3'),
    path('gradinite_stat/sector4', views.gradinite_stat_sector4, name='gradinite_stat/sector4'),
    path('gradinite_stat/sector5', views.gradinite_stat_sector5, name='gradinite_stat/sector5'),
    path('gradinite_stat/sector6', views.gradinite_stat_sector6, name='gradinite_stat/sector6'),
    path('gradinite_stat/ilfov', views.gradinite_stat_ilfov, name='gradinite_stat/ilfov'),

    path('inscriere/', views.inscriere, name='inscriere'),
    path('contact/', views.contact, name='contact'),
]
