from django import forms
from .models import VoyageCarte
import re
from datetime import datetime
from datetime import date
from django.utils.dateparse import parse_date

class VoyageCarteForm(forms.ModelForm):
    FAVORITE_COLORS_CHOICES = (
    ("AF" , 'Afghanistan'),
    ("AL" , 'Albania'),
    ("DZ" , 'Algeria'),
    ("AO" , 'Angola'),
    ("AG" , 'Antigua and Barbuda'),
    ("AR" , 'Argentina'),
    ("AM" , 'Armenia'),
    ("AU" , 'Australia'),
    ("AT" , 'Austria'),
    ("AZ" , 'Azerbaijan'),
    ("BS" , 'Bahamas'),
    ("BH" , 'Bahrain'),
    ("BD" , 'Bangladesh'),
    ("BB" , 'Barbados'),
    ("BY" , 'Belarus'),
    ("BE" , 'Belgium'),
    ("BZ" , 'Belize'),
    ("BJ" , 'Benin'),
    ("BT" , 'Bhutan'),
    ("BO" , 'Bolivia'),
    ("BA" , 'Bosnia and Herzegovina'),
    ("BW" , 'Botswana'),
    ("BR" , 'Brazil'),
    ("BN" , 'Brunei'),
    ("BG" , 'Bulgaria'),
    ("BF" , 'Burkina Faso'),
    ("BI" , 'Burundi'),
    ("KH" , 'Cambodia'),
    ("CM" , 'Cameroon'),
    ("CA" , 'Canada'),
    ("CV" , 'Cape Verde'),
    ("CF" , 'Central African Republic'),
    ("TD", 'Chad'),
    ("CL", 'Chile'),
    ("CN", 'China'),
    ("CO", 'Colombia'),
    ("KM", 'Comoros'),
    ("CD", 'Democratic Republic of the Congo'),
    ("CG", 'Republic of the Congo'),
    ("CR", 'Costa Rica'),
    ("CI", 'Ivory Coast'),
    ("HR", 'Croatia'),
    ("CY", 'Cyprus'),
    ("CZ", 'Czech Republic'),
    ("DK", 'Denmark'),
    ("DJ", 'Djibouti'),
    ("DM", 'Dominica'),
    ("DO", 'Dominican Republic'),
    ("EC", 'Ecuador'),
    ("EG", 'Egypt'),
    ("SV", 'El Salvador'),
    ("GQ", 'Equatorial Guinea'),
    ("ER", 'Eritrea'),
    ("EE", 'Estonia'),
    ("ET", 'Ethiopia'),
    ("FJ" , 'Fiji'),
    ("FI" , 'Finland'),
    ("FR" , 'France'),
    ("GA" , 'Gabon'),
    ("GM" , 'Gambia'),
    ("GE" , 'Georgia'),
    ("DE" , 'Germany'),
    ("GH" , 'Ghana'),
    ("GR" , 'Greece'),
    ("GD" , 'Grenada'),
    ("GT" , 'Guatemala'),
    ("GN" , 'Guinea'),
    ("GW" , 'Guinea-Bissau'),
    ("GY" , 'Guyana'),
    ("HT" , 'Haiti'),
    ("HN" , 'Honduras'),
    ("HK" , 'Hong Kong'),
    ("HU" , 'Hungary'),
    ("IS" , 'Iceland'),
    ("IN" , 'India'),
    ("ID" , 'Indonesia'),
    ("IR" , 'Iran'),
    ("IQ" , 'Iraq'),
    ("IE" , 'Ireland'),
    ("IT" , 'Italy'),
    ("JM" , 'Jamaica'),
    ("JP" , 'Japan'),
    ("JO" , 'Jordan') ,
    ("KZ" , 'Kazakhstan') ,
    ("KE" , 'Kenya') ,
    ("KI" , 'Kiribati' ),
    ("KR" , 'South Korea') ,
    ("KW" , 'Kuwait') ,
    ("KG" , 'Kyrgyzstan') ,
    ("LA" , 'Laos') ,
    ("LV" , 'Latvia') ,
    ("LB" , 'Lebanon' ),
    ("LS" , 'Lesotho') ,
    ("LR" , 'Liberia') ,
    ("LY" , 'Libya') ,
    ("LT" , 'Lithuania') ,
    ("LU" , 'Luxembourg') ,
    ("MK" , 'Macedonia') ,
    ("MG" , 'Madagascar') ,
    ("MW" , 'Malawi') ,
    ("MY" , 'Malaysia') ,
    ("MV" , 'Maldives') ,
    ("ML" , 'Mali') ,
    ("MT" , 'Malta') ,
    ("MR" , 'Mauritania') ,
    ("MU" , 'Mauritius') ,
    ("MX" , 'Mexico') ,
    ("MD" , 'Moldova') ,
    ("MN" , 'Mongolia') ,
    ("ME" , 'Montenegro') ,
    ("MA" , 'Morocco') ,
    ("MZ" , 'Mozambique') ,
    ("MM" , 'Myanmar') ,
    ("NA" , 'Namibia') ,
    ("NP" , 'Nepal') ,
    ("NL" , 'Netherlands') ,
    ("NZ" , 'New Zealand') ,
    ("NI" , 'Nicaragua') ,
    ("NE" , 'Niger') ,
    ("NG" , 'Nigeria') ,
    ("NO" , 'Norway') ,
    ("OM" , 'Oman') ,
    ("PK" , 'Pakistan') ,
    ("PA" , 'Panama') ,
    ("PG" , 'Papua New Guinea') ,
    ("PY" ,  'Paraguay') ,
    ("PE" ,  'Peru') ,
    ("PH" ,  'Philippines') ,
    ("PL" ,  'Poland') ,
    ("PT" ,  'Portugal') ,
    ("QA" ,  'Qatar') ,
    ("RO" ,  'Romania') ,
    ("RU" ,  'Russia') ,
    ("RW" ,  'Rwanda') ,
    ("WS" ,  'Samoa') ,
    ("ST" ,  'Sao Tome and Principe') ,
    ("SA" ,  'Saudi Arabia') ,
    ("SN" ,  'Senegal') ,
    ("RS" ,  'Serbia') ,
    ("SC" ,  'Seychelles') ,
    ("SL" ,  'Sierra Leone') ,
    ("SG" ,  'Singapore') ,
    ("SK" ,  'Slovakia') ,
    ("SI" ,  'Slovenia') ,
    ("SB" ,  'Solomon Islands') ,
    ("ZA" , 'South Africa') ,
    ("ES" , 'Spain') ,
    ("LK" , 'Sri Lanka') ,
    ("KN" , 'Saint Kitts and Nevis') ,
    ("LC" , 'Saint Lucia') ,
    ("VC" , 'Saint Vincent and the Grenadines') ,
    ("SD" , 'Sudan') ,
    ("SR" , 'Suriname') ,
    ("SZ" , 'Swaziland') ,
    ("SE" , 'Sweden') ,
    ("CH" , 'Switzerland') ,
    ("SY" , 'Syria') ,
    ("TW" , 'Taiwan') ,
    ("TJ" , 'Tajikistan') ,
    ("TZ" , 'Tanzania') ,
    ("TH" , 'Thailand') ,
    ("TL" , 'East Timor') ,
    ("TG" , 'Togo') ,
    ("TO" , 'Tonga') ,
    ("TT" , 'Trinidad and Tobago'),
    ("TN" , 'Tunisia'),
    ("TR" , 'Turkey'),
    ("TM" , 'Turkmenistan'),
    ("UG" , 'Uganda'),
    ("UA" , 'Ukraine'),
    ("AE" , 'United Arab Emirates'),
    ("GB" , 'United Kingdom'),
    ("US" , 'United States'),
    ("UY" , 'Uruguay'),
    ("UZ" , 'Uzbekistan'),
    ("VU" , 'Vanuatu'),
    ("VE" , 'Venezuela'),
    ("VN" , 'Vietnam'),
    ("YE" , 'Yemen'),
    ("ZM" , 'Zambia'),
    ("ZW" , 'Zimbabwe'),
    )
    destination=forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control pay'}),choices=FAVORITE_COLORS_CHOICES)
    ville=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'La ville de mes réves'}))
    dateAller=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control date','placeholder':'jj/mm/aa'}))
    dateRetour=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control date','placeholder':'jj/mm/aa'}))
    nbrAdulte=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','value':'1'}))
    nbrEnfant=forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control','value':'0'}))
    message=forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Mon voyage en quelque mots'}))
    nom=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Mon nom'}))
    prenom=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Mon Prénom'}))
    telephone=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Mon numero'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder':'Mon adresse mail'}))
    class Meta:
        model=VoyageCarte
        fields=[
        'nom','prenom','email','message','telephone',
        'destination','ville','dateAller','dateRetour',
        'nbrAdulte','nbrEnfant'
        ]
    def is_valid(self):
        valid = super(VoyageCarteForm, self).is_valid()
        if not valid:
            return valid
        dater=datetime.strptime(self.cleaned_data.get('dateRetour'), "%Y-%m-%d").date()
        datea=datetime.strptime(self.cleaned_data.get('dateAller'), "%Y-%m-%d").date()
        if dater<datea:
            self.add_error('dateRetour', 'Date Retour Invalide')
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
