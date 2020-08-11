"""mechts URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from sbiv_mechts import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('svadba/scenariy', views.scenariy),
    path('', views.index),
    path('svadba', views.svadba),
    path('lk', views.lk),
    path('artist', views.artist),
    path('katalog', views.katalog),
    path('classic', views.classic),

    path('viez_registric', views.viez_registric),
    path('scenariy', views.scenariy),

    path('uslugi', views.uslugi),
    path('ofic', views.ofic),
    path('rab', views.rab),
    path('lk_korzina', views.lk_korzina),

]
