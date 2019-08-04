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
        ]
    def is_valid(self):
        valid = super(BilletrieForm, self).is_valid()
        if not valid:
            return valid
        datea=datetime.strptime(self.cleaned_data.get('dateAller'), "%Y-%m-%d").date()
        if self.cleaned_data.get('dateRetour') is not None:
            dater=datetime.strptime(self.cleaned_data.get('dateRetour') , "%Y-%m-%d").date()

        try:
            if dater<datea:
                self.add_error('dateRetour', 'Date Retour Invalide')
        except NameError: dater = None
        if datea<datetime.now().date():
             self.add_error('dateAller', 'Date Aller Invalide')



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
