from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import ContactForm
# Create your views here.
class Contact(TemplateView):
    def get(self,request):
        form=ContactForm()
        return render(request,'contact/contact.html',{'form':form})
    def post(self,request):
        form=ContactForm(request.POST or None)
        social=Social.objects.get(id=1)
        if form.is_valid():
            form.save()
            return render(request,'contact/contact.html',{'message':'Merci , Nous prenons en charge votre demande'})
        else :
            return render(request,'contact/contact.html',{'form':form,'message':'Erreur Validation'})
