from django.contrib import admin
from .models import VoyageCarte
# Register your models here.


class VoyageCarteAdmin(admin.ModelAdmin):
    list_display = ('recu','destination','telephone', 'email','dateAller','dateRetour')
    list_filter = ('recu', )
    readonly_fields = ['recu','destination','telephone', 'email','dateAller','dateRetour','nom','prenom','ville','nbrAdulte','nbrEnfant','message']
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(VoyageCarte,VoyageCarteAdmin)
