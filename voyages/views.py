from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.conf import settings
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.core.paginator import Paginator
import os
from datetime import datetime
# Create your views here.

class HomeVoyages(TemplateView):
    def get(self,request):
        voyages_list=Voyage.objects.all()
        paginator = Paginator(voyages_list, 12) # Show 25 contacts per page
        page = request.GET.get('page')
        voyages = paginator.get_page(page)
        return render(request,'voyages/home.html', {'search':filter,'voyages':voyages,'voyages_all_count':voyages_list.count()})


class SingleVoyage(TemplateView):
    def get(self,request,slug):
        voyage=Voyage.objects.filter(slug=slug).first()
        random=Voyage.objects.order_by('?')[:10]
        return render(request,'voyages/single_voyages.html', {'voyage':voyage,'randoms':random})
