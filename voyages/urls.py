from django.contrib import admin
from django.urls import path,include,re_path
from . import views


urlpatterns = [
        re_path(r'^$', views.HomeVoyages.as_view(),name='voyages_acceuil'),
        path('<str:slug>/details', views.SingleVoyage.as_view(),name='single_voyages'),
]
