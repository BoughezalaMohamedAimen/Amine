from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('recu','nom','prenom','telephone', 'email','message')
    list_filter = ('recu', )
    readonly_fields = ['recu','telephone', 'email','nom','prenom','message']
    def has_add_permission(self, request, obj=None):
        return False
    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Contact,ContactAdmin)
