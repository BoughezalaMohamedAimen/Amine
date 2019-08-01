from django import forms
from django.forms import ModelForm
from .models import *
import operator
# from django_countries.fields import CountryField
from django_countries.data import COUNTRIES

WILAYA_CHOICES=(('16','Alger'),('9','Blida'),('42','Tipaza'),('35','Boumerdes'))


class FilterForm(forms.Form):
    destination=forms.CharField(widget=forms.Select(
    choices =sorted(COUNTRIES.items(),key=operator.itemgetter(1)),
    attrs={
    'class': 'selectpicker form-control bg-white border filterr',
    'multiple':'',
    'data-live-search':'true',
    'title':'Selectioner Pays'
    }),required='false')
    wilaya=forms.CharField(widget=forms.Select(choices =WILAYA_CHOICES,
    attrs={
    'class': 'selectpicker form-control bg-white border filterr',
    'multiple':'',
    'data-live-search':'true',
    'title':'Wilaya'
    }),required=False)
    minprice=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control filterr'}),required=False)
    maxprice=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control filterr'}),required=False)
    mincommission=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control filterr'}),required=False)
    maxcommission=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control filterr'}),required=False)
    mot_cle=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control filterr'}),required=False)




class VisaForm(ModelForm):
    destination=forms.CharField(widget=forms.Select(
    choices =sorted(COUNTRIES.items(),key=operator.itemgetter(1)),attrs={
    'class': 'selectpicker form-control bg-white border',
    'data-live-search':'true',
    'title':'Destination'
    }),)

    class Meta:
        model=Visa
        exclude=['slug',]


class VisaFormUpdate(ModelForm):
    destination=forms.CharField(widget=forms.Select(
    choices =sorted(COUNTRIES.items(),key=operator.itemgetter(1)),attrs={
    'class': 'selectpicker form-control bg-white border',
    'data-live-search':'true',
    'title':'Destination'
    }),)

    class Meta:
        model=Visa
        exclude=['user','slug']
