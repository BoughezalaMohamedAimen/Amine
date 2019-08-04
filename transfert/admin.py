from django.contrib import admin
from .models import *
# Register your models here.


class TransfertAdmin(admin.ModelAdmin):
    list_display = ('recu','depart','arrive','telephone','nom')
    list_filter = ('recu','depart','arrive' )
    fields = ('recu','depart','arrive', 'dateAller','dateRetour','nbrAdulte',)
    # readonly_fields = ['recu','destination','telephone', 'email','dateAller','dateRetour','nom','prenom','ville','nbrAdulte','nbrEnfant','nbrChambre']
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def get_readonly_fields(self, request, obj=None):
        # make all fields readonly
        readonly_fields = list(set(
            [field.name for field in self.opts.local_fields] +
            [field.name for field in self.opts.local_many_to_many]
        ))
        if 'is_submitted' in readonly_fields:
            readonly_fields.remove('is_submitted')
        return readonly_fields




admin.site.register(Transfert,TransfertAdmin)
