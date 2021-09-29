from rest_framework import serializers
from .models import Citizen, Project, Form, DataEntry, DataVis, Post

class CitizenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citizen
        fields = ('id', 'name','password','img','bio',)

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'header', 'img', 'creator', 'admin_list', 'contributor_list', 'description', 'private', 'active', 'date_created')

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ('id', 'project', 'creator', 'int1', 'int2', 'int3', 'int4', 'int1_label', 'int2_label', 'int3_label', 'int4_label', 'float1', 'float2', 'float3', 'float4', 'float1_label', 'float2_label', 'float3_label', 'float4_label', 'img_url', 'img_label', 'dropdown1', 'dropdown2', 'dropdown1_label', 'dropdown2_label', 'dropdownOptions1', 'dropdownOptions2', 'notes', 'latlon', 'zipcode', 'date_created')

class DataEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = DataEntry
        fields = ('id', 'project', 'contributor', 'int1', 'int2', 'int3', 'int4', 'int1_label', 'int2_label', 'int3_label', 'int4_label', 'float1', 'float2', 'float3', 'float4', 'float1_label', 'float2_label', 'float3_label', 'float4_label', 'img_url', 'img_label', 'dropdown1', 'dropdown2', 'dropdown1_label', 'dropdown2_label', 'notes', 'lat', 'lon', 'zipcode',)

class DataVisSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataVis
        fields = ('id', 'project', 'contributor', 'chart_type', 'chart_title', 'x_axis', 'x_axis_min', 'x_axis_max', 'y_axis', 'y_axis_min', 'y_axis_max', 'legend', 'pie_hole')

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('project', 'author', 'title', 'body', 'pinned', 'date_posted')