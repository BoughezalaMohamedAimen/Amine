from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import HotelForm
# Create your views here.


class hotels(TemplateView):
    def get(self,request):
        form=HotelForm()
        return render(request,'hotel/hotel.html',{'form':form })
    def post(self,request):
        form=HotelForm(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request,'hotel/hotel.html',{'message':'Merci , Nous prenons en charge votre demande'})
        else :
            return render(request,'hotel/hotel.html',{'form':form,'message':'erreur Validation'})
