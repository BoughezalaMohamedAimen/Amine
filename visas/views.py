from django.shortcuts import render,redirect
from django.views.generic import TemplateView

from .forms import *


from .models import *
from django.core.paginator import Paginator

from datetime import datetime
# Create your views here.


class HomeVisas(TemplateView):
    def get(self,request):
        visas_list=Visa.objects.all()
        paginator = Paginator(visas_list, 12) # Show 25 contacts per page
        page = request.GET.get('page')
        visas = paginator.get_page(page)
        return render(request,'visas/home.html', {'visas':visas,'visas_all_count':visas_list.count()})




class SingleVisa(TemplateView):
    def get(self,request,slug):
        visa=Visa.objects.filter(slug=slug).first()
        random=Visa.objects.order_by('?')[:10]
        return render(request,'visas/single_visas.html', {'visa':visa,'randoms':random})
