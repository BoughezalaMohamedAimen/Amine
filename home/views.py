from django.shortcuts import render
from .models import *
from voyages.models import *
# Create your views here.
def Home(request):
    slides=Slider.objects.all()
    voyages=Voyage.objects.order_by('?')[:10]
    return render(request,'home/home.html',{'slides':slides,'voyages':voyages})
