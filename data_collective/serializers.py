from rest_framework import serializers
from .models import Citizen, Project, Form, DataEntry

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = ('id', 'name','password','img','bio',)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'header', 'img', 'creator', 'admin_list', 'contributor_list', 'description',)

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('id', 'project', 'creator', 'int1', 'int2', 'int3', 'int4', 'int1_label', 'int2_label', 'int3_label', 'int4_label', 'float1', 'float2', 'float3', 'float4', 'float1_label', 'float2_label', 'float3_label', 'float4_label', 'img_url', 'img_label', 'dropdown1', 'dropdown2', 'dropdown1_label', 'dropdown2_label', 'dropdownOptions1', 'dropdownOptions2', 'notes', 'latlon', 'zipcode', 'date_created')

class DataEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataEntry
        fields = ('id', 'project', 'contributor', 'int1', 'int2', 'int3', 'int4', 'float1', 'float2', 'float3', 'float4', 'img_url', 'dropdown1', 'dropdown2', 'notes', 'lat', 'lon', 'zipcode',)