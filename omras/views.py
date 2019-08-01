from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.conf import settings
from .forms import *
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.core.paginator import Paginator
import os
from datetime import datetime
# Create your views here.


class HomeOmras(TemplateView):
    def get(self,request):
        omras_list=Omra.objects.all()
        paginator = Paginator(omras_list, 12) # Show 25 contacts per page
        page = request.GET.get('page')
        omras = paginator.get_page(page)
        return render(request,'omras/home.html', {'omras':omras,'omras_all_count':omras_list.count()})




class SingleOmra(TemplateView):
    def get(self,request,slug):
        omra=Omra.objects.filter(slug=slug).first()
        random=Omra.objects.order_by('?')[:10]
        return render(request,'omras/single_omras.html', {'omra':omra,'randoms':random})
