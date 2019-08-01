from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import VoyageCarteForm
class Carte(TemplateView):
    def get(self,request):
        form=VoyageCarteForm()
        return render(request,'VoyageCarte/carte.html',{'form':form})
    def post(self,request):
        form=VoyageCarteForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request,'VoyageCarte/carte.html',{'message':'Merci , Nous prenons en charge votre demande'})
        else :
            return render(request,'VoyageCarte/carte.html',{'form':form,'message':'erreur Validation'})
