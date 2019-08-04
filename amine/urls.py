"""amine URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.contrib import admin
from billetrie.views import Billeterie
from transfert.views import Transferts
from hotel.views import hotels
from home.views import Home
from VoyageCarte.views import Carte
from contact.views import Contact


from .sitemaps import *
from django.contrib.sitemaps.views import sitemap



sitemaps={
    'voyages':VoyageSitemap,
    'omras':OmraSitemap,
    'visas':VisaSitemap,
    'static':staticSitemap,
}

urlpatterns = [
    path('sitemap.xml', sitemap,{'sitemaps':sitemaps}),
    path('admin/', admin.site.urls),
    path('voyages/', include('voyages.urls')),
    path('omras/', include('omras.urls')),
    path('visas/', include('visas.urls')),
    path('',Home,name='home'),
    path('services/billeterie/', Billeterie.as_view(),name='billeterie'),
    path('services/transfert/', Transferts.as_view(),name='transfert'),
    path('services/hotel/', hotels.as_view(),name='hotel'),
    path('services/voyage-a-la-carte/', Carte.as_view(),name='carte'),
    path('contact/', Contact.as_view(),name='contact'),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header='Administration du Site'
