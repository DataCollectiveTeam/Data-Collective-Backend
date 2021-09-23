from django.contrib import admin

# Register your models here.
from .models import Citizen, Project, Form, DataEntry
admin.site.register(Citizen)
admin.site.register(Project)
admin.site.register(Form)
admin.site.register(DataEntry)