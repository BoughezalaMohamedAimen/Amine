from django import forms
from .models import Contact
import re
from datetime import datetime
from datetime import date

class ContactForm(forms.ModelForm):

    message=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','rows':'4'}))
    nom=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Votre nom'}))
    prenom=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Votre Prénom'}))
    telephone=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Votre Télephone'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Votre adresse mail'}))
    class Meta:
        model=Contact
        fields=[
        'nom','prenom','email','message','telephone',
        ]
    def is_valid(self):
        valid = super(ContactForm, self).is_valid()
        if not valid:
            return valid

        mobile = re.compile(r'^0[5-9][0-9]{8}')
        fix=re.compile(r'^0[2-9][0-9]{7}')
        phone=self.cleaned_data.get('telephone')
        if (not mobile.search(phone)) and (not fix.search(phone)):
            self.add_error('telephone', 'Numero de Telephone Invalide')


        if not self.errors:
            return True
        return False
