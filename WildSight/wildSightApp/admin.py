from django.contrib import admin

# Register your models here.

from .models import Location, Species

admin.site.register(Location)
admin.site.register(Species)