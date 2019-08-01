from django.contrib import admin
from django.urls import path,include,re_path
from . import views


urlpatterns = [
        re_path(r'^$', views.HomeOmras.as_view(),name='omras_acceuil'),
        path('<str:slug>/details', views.SingleOmra.as_view(),name='single_omras'),
]
