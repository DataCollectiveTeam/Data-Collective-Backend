from django.db import models
from datetime import datetime
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Citizen(models.Model):
    name = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    img = models.URLField()
    bio = models.CharField(max_length=200)
    account_created = models.DateTimeField(default=datetime.now, blank=True)
    projects_count = models.IntegerField(default=0)
    contributions_count = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=40)
    header = models.CharField(max_length=100)
    img = models.URLField()
    creator = models.ForeignKey(Citizen, on_delete=models.DO_NOTHING, related_name='projects')
    admin_list = models.ManyToManyField(Citizen, related_name='administrators')
    contributor_list = models.ManyToManyField(Citizen, related_name='contributors')
    description = models.TextField()
    private = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name

class DataEntry(models.Model):
    project = ForeignKey(Project, on_delete=models.CASCADE, related_name='data_entries')
    contributor = models.ForeignKey(Citizen, on_delete=models.DO_NOTHING, related_name='entries')
    int1 = models.IntegerField(null=True, blank=True)
    int2 = models.IntegerField(null=True, blank=True)
    int3 = models.IntegerField(null=True, blank=True)
    int4 = models.IntegerField(null=True, blank=True)
    float1 = models.FloatField(null=True, blank=True)
    float2 = models.FloatField(null=True, blank=True)
    float3 = models.FloatField(null=True, blank=True)
    float4 = models.FloatField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    img_url = models.URLField(default='', blank=True)
    dropdown1 = models.TextField(default='', blank=True)
    dropdown2 = models.TextField(default='', blank=True)
    notes = models.TextField(default='', blank=True)
    lat = models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True)
    lon = models.DecimalField(null=True, max_digits=9, decimal_places=6, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.date_created