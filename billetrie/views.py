from django.shortcuts import render
from .forms import BilletrieForm
from django.views.generic import TemplateView
# Create your views here.

class Billeterie(TemplateView):
    def get(self,request):
        form=BilletrieForm()
        return render(request,'billetrie/billetrie.html',{'form':form})
    def post(self,request):
        form=BilletrieForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request,'billetrie/billetrie.html',{'message':'Merci , Nous prenons en charge votre demande'})
        else :
            return render(request,'billetrie/billetrie.html',{'form':form,'message':'Erreur Validation'})
