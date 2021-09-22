from rest_framework import serializers
from .models import Citizen, Project, DataEntry

class CitizenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Citizen
        fields = ('id', 'name','password','img','bio',)


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id', 'name', 'header', 'img', 'creator', 'admin_list', 'contributor_list', 'description',)


class DataEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = DataEntry
        fields = ('id', 'project', 'contributor', 'int1', 'int2', 'int3', 'int4', 'float1', 'float2', 'float3', 'float4', 'notes', 'lat', 'long', 'zipcode',)