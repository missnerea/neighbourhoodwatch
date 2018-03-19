from django.contrib import admin
from .models import Neighbourhood , Business

class NeighbourhoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'location']

    def related_business(self, obj):
        return obj.businessid.name
    related_business.short_description = 'Business'

# Register your models here.
admin.site.register(Neighbourhood,NeighbourhoodAdmin)