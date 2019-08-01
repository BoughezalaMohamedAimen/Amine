from django.contrib import admin
from django.urls import path,include,re_path
from . import views


urlpatterns = [
        re_path(r'^$', views.HomeVisas.as_view(),name='visas_acceuil'),
        path('<str:slug>/details', views.SingleVisa.as_view(),name='single_visas'),
]
