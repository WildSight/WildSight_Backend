from django.contrib import admin

# Register your models here.

from .models import Location, Species, Refined_Sighting, Raw_Sighting

admin.site.register(Location)
admin.site.register(Species)
admin.site.register(Refined_Sighting)
admin.site.register(Raw_Sighting)