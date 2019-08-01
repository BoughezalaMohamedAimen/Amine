from django import forms
from .models import Billeterie
import re
from datetime import datetime
from datetime import date
from django.utils.dateparse import parse_date

class BilletrieForm(forms.ModelForm):
    CLASSE_CHOICES = (
    ("economique" , 'Economique'),
    ("affaire" , 'Affaire'),
    ("premiere" , 'Premiére'),
    )
    depart=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Aéroport depart','id':'autocomplete'}))
    arrive=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Aéroport arrivé','id':'autocomplete2'}))
    classe=forms.CharField(widget=forms.Select(attrs={'class': 'form-control pay'},choices=CLASSE_CHOICES))
    dateAller=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control date date1','placeholder':'jj/mm/aa'}))
    dateRetour=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control date date2','placeholder':'jj/mm/aa'}),required = False)
    nbrAdulte=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','value':'1'}))
    nbrEnfant=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','value':'0'}))


    depart_multiple=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Aéroport depart','id':'autocomplete3'}),required = False)
    arrive_multiple=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Aéroport arrivé','id':'autocomplete4'}),required = False)
    classe_multiple=forms.CharField(widget=forms.Select(attrs={'class': 'form-control pay'},choices=CLASSE_CHOICES))
    dateAller_multiple=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control date date11','placeholder':'jj/mm/aa'}),required = False)
    dateRetour_multiple=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control date date22','placeholder':'jj/mm/aa'}),required = False)
    nbrAdulte_multiple=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','value':'1'}))
    nbrEnfant_multiple=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','value':'0'}))


    nom=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Votre nom'}))
    prenom=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Votre Prénom'}))
    telephone=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Votre numero'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Votre adresse mail'}))
    class Meta:
        model=Billeterie
        fields=[
        'nom','prenom','email','telephone',
        'depart','arrive','dateAller','dateRetour','classe',
        'nbrAdulte','nbrEnfant',
        'depart_multiple','arrive_multiple','dateAller_multiple','dateRetour_multiple','classe_multiple',
        'nbrAdulte_multiple','nbrEnfant_multiple',
        ]
    def is_valid(self):
        valid = super(BilletrieForm, self).is_valid()
        if not valid:
            return valid
        datea=datetime.strptime(self.cleaned_data.get('dateAller'), "%Y-%m-%d").date()
        if self.cleaned_data.get('dateRetour') is not None:
            dater=datetime.strptime(self.cleaned_data.get('dateRetour') , "%Y-%m-%d").date()
        if self.cleaned_data.get('dateRetour_multiple') is not None:
            daterm=datetime.strptime(self.cleaned_data.get('dateRetour_multiple') , "%Y-%m-%d").date()
        if self.cleaned_data.get('dateAller_multiple') is not None:
            dateam=datetime.strptime(self.cleaned_data.get('dateAller_multiple') , "%Y-%m-%d").date()
        try:
            if dater<datea:
                self.add_error('dateRetour', 'Date Retour Invalide')
        except NameError: dater = None
        if datea<datetime.now().date():
             self.add_error('dateAller', 'Date Aller Invalide')
        try:
            if daterm<datea and daterm is not None:
                self.add_error('dateRetour_multiple', 'Date Retour Multiple Invalide')
        except NameError: daterm = None
        try:
            if dateam<datea and dateam is not None:
                self.add_error('dateAller_multiple', 'Date Aller Multiple Invalide')
        except NameError: dateam = None
        try:
            if  daterm is not None and dateam is not None:
                if daterm<dateam:
                    self.add_error('dateRetour_multiple', 'Date Retour Multiple Invalide')
        except NameError: daterm = None
        except NameError: datem = None

        mobile = re.compile(r'^0[5-9][0-9]{8}')
        fix=re.compile(r'^0[2-9][0-9]{7}')
        phone=self.cleaned_data.get('telephone')
        if (not mobile.search(phone)) and (not fix.search(phone)):
            self.add_error('telephone', 'Numero de Telephone Invalide')


        if not self.errors:
            return True
        return False

    def clean_dateRetour(self):
        if self.cleaned_data.get('dateRetour')!='':
            return self.cleaned_data.get('dateRetour')
        else:
            return None;
    def clean_dateAller_multiple(self):
        if self.cleaned_data.get('dateAller_multiple')!='':
            return self.cleaned_data.get('dateAller_multiple')
        else:
            return None;
    def clean_dateRetour_multiple(self):
        if self.cleaned_data.get('dateRetour_multiple')!='':
            return self.cleaned_data.get('dateRetour_multiple')
        else:
            return None;
