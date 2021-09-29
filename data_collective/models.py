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

class Form(models.Model):
    project = ForeignKey(Project, on_delete=models.CASCADE, related_name='form')
    creator = models.ForeignKey(Citizen, on_delete=models.DO_NOTHING, related_name='forms')

    int1 = models.BooleanField(default=False)
    int2 = models.BooleanField(default=False)
    int3 = models.BooleanField(default=False)
    int4 = models.BooleanField(default=False)
    int1_label = models.CharField(max_length=40, default='', blank=True)
    int2_label = models.CharField(max_length=40, default='', blank=True)
    int3_label = models.CharField(max_length=40, default='', blank=True)
    int4_label = models.CharField(max_length=40, default='', blank=True)

    float1 = models.BooleanField(default=False)
    float2 = models.BooleanField(default=False)
    float3 = models.BooleanField(default=False)
    float4 = models.BooleanField(default=False)
    float1_label = models.CharField(max_length=40, default='', blank=True)
    float2_label = models.CharField(max_length=40, default='', blank=True)
    float3_label = models.CharField(max_length=40, default='', blank=True)
    float4_label = models.CharField(max_length=40, default='', blank=True)

    img_url = models.BooleanField(default=False)
    img_label = models.CharField(max_length=40, default='', blank=True)

    dropdown1 = models.BooleanField(default=False)
    dropdown2 = models.BooleanField(default=False)
    dropdown1_label = models.CharField(max_length=40, default='', blank=True)
    dropdown2_label = models.CharField(max_length=40, default='', blank=True)
    dropdownOptions1 = models.TextField(default='', blank=True)
    dropdownOptions2 = models.TextField(default='', blank=True)

    notes = models.BooleanField(default=False)

    latlon = models.BooleanField(default=False)
    zipcode = models.BooleanField(default=False)

    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.date_created

class DataEntry(models.Model):
    project = ForeignKey(Project, on_delete=models.CASCADE, related_name='data_entries')
    contributor = models.ForeignKey(Citizen, on_delete=models.DO_NOTHING, related_name='entries')

    int1 = models.IntegerField(null=True)
    int2 = models.IntegerField(null=True)
    int3 = models.IntegerField(null=True)
    int4 = models.IntegerField(null=True)

    int1_label = models.CharField(max_length=40, default='', blank=True)
    int2_label = models.CharField(max_length=40, default='', blank=True)
    int3_label = models.CharField(max_length=40, default='', blank=True)
    int4_label = models.CharField(max_length=40, default='', blank=True)

    float1 = models.FloatField(null=True)
    float2 = models.FloatField(null=True)
    float3 = models.FloatField(null=True)
    float4 = models.FloatField(null=True)

    float1_label = models.CharField(max_length=40, default='', blank=True)
    float2_label = models.CharField(max_length=40, default='', blank=True)
    float3_label = models.CharField(max_length=40, default='', blank=True)
    float4_label = models.CharField(max_length=40, default='', blank=True)

    img_url = models.URLField(default='', blank=True)
    img_label = models.CharField(max_length=40, default='', blank=True)

    dropdown1 = models.TextField(default='', blank=True)
    dropdown2 = models.TextField(default='', blank=True)

    dropdown1_label = models.CharField(max_length=40, default='', blank=True)
    dropdown2_label = models.CharField(max_length=40, default='', blank=True)

    notes = models.TextField(default='', blank=True)
    
    lat = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    lon = models.DecimalField(null=True, max_digits=9, decimal_places=6)
    zipcode = models.CharField(max_length=10, blank=True, default='')

    date_created = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.date_created

class DataVis(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='data_visualizations')
    contributor = models.ForeignKey(Citizen, on_delete=models.DO_NOTHING, related_name='citizen')

    chart_type = models.CharField(max_length=100)
    chart_title = models.CharField(max_length=150)

    x_axis = models.CharField(max_length=100)
    x_axis_min = models.IntegerField(null=True)
    x_axis_max = models.IntegerField(null=True)

    y_axis = models.CharField(max_length=100)
    y_axis_min = models.IntegerField(null=True)
    y_axis_max = models.IntegerField(null=True)

    legend = models.BooleanField(default=True)

    pie_hole = models.FloatField(null=True)

    def __str__(self):
        return self.chart_title

class Post(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='discussions')
    author = models.ForeignKey(Citizen, on_delete=models.DO_NOTHING, related_name='posts')
    username = models.CharField(max_length=40)

    title = models.CharField(max_length=150)
    body = models.TextField(max_length=500)

    pinned = models.BooleanField(default=False)

    date_posted = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title


