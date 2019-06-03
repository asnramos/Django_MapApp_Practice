from django.contrib import admin
from .models import Incidences
from leaflet.admin import LeafletGeoAdmin

# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    pass
    """
    list_display = ('name', 'location', 'objects', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    """

admin.site.register(Incidences, IncidencesAdmin)

