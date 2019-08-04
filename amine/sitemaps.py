from django.contrib.sitemaps import Sitemap

from voyages.models import Voyage
from omras.models import Omra
from visas.models import Visa
from django.urls import reverse


class VoyageSitemap(Sitemap):
    changefreq='monthly'
    priority=0.5

    def items(self):
        return Voyage.objects.all()

class OmraSitemap(Sitemap):
    changefreq='monthly'
    priority=0.5

    def items(self):
        return Omra.objects.all()


class VisaSitemap(Sitemap):
    changefreq='monthly'
    priority=0.5

    def items(self):
        return Visa.objects.all()

class staticSitemap(Sitemap):
    def items(Self):
        return ['home','contact','billeterie','transfert','hotel','carte']

    def location(self,item):
        return reverse(item)
