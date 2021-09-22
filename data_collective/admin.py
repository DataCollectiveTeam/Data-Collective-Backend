from django.contrib import admin

# Register your models here.
from .models import Citizen, Project, DataEntry
admin.site.register(Citizen)
admin.site.register(Project)
admin.site.register(DataEntry)