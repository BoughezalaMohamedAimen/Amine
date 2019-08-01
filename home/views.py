from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    slides=Slider.objects.all()
    return render(request,'home/home.html',{'slides':slides})
