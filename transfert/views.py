from django.shortcuts import render
from .forms import TransfertForm
from django.views.generic import TemplateView
# Create your views here.

class Transferts(TemplateView):
    def get(self,request):
        form=TransfertForm()
        return render(request,'transfert/transfert.html',{'form':form })
    def post(self,request):
        form=TransfertForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request,'transfert/transfert.html',{'message':'Merci , Nous prenons en charge votre demande'})
        else :
            return render(request,'transfert/transfert.html',{'form':form,'message':'Erreur Validation'})
