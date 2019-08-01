from django import forms
from django.forms import ModelForm
from .models import *
import operator
# from django_countries.fields import CountryField


WILAYA_CHOICES=(('16','Alger'),('9','Blida'),('42','Tipaza'),('35','Boumerdes'))


class FilterForm(forms.Form):

    mindate=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control datetimepicker-input filterr','data-target':'#datetimepicker7'}),required=False)
    maxdate=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control datetimepicker-input filterr','data-target':'#datetimepicker8'}),required=False)
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
    distance_kaaba=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control filterr'}),required=False)
    distance_masjid=forms.CharField(widget=forms.NumberInput(attrs={'class':'form-control filterr'}),required=False)
    mot_cle=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control filterr'}),required=False)




class OmraForm(ModelForm):
    aller=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control datetimepicker-input','data-target':'#datetimepicker7'}))
    retour=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control datetimepicker-input','data-target':'#datetimepicker8'}))

    class Meta:
        model=Omra
        exclude=['slug',]


class OmraFormUpdate(ModelForm):
    aller=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control datetimepicker-input','data-target':'#datetimepicker7'}))
    retour=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control datetimepicker-input','data-target':'#datetimepicker8'}))

    class Meta:
        model=Omra
        exclude=['user','slug']
