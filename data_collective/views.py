from django.db.models import manager
from rest_framework import filters, generics
from .models import Citizen, Project, Form, DataEntry, DataVis, Post
from .serializers import CitizenSerializer, ProjectSerializer, FormSerializer, DataEntrySerializer, DataVisSerializer, PostSerializer

# View Classes
class CitizenList(generics.ListCreateAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

class AList(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Project.objects.filter(admin_list__in=id)

class Contributions(generics.ListAPIView):
    serializer_class = ProjectSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        match = Project.objects.filter(contributor_list__in=id)
        return match

class CitizenLogin(generics.ListAPIView):
    serializer_class = CitizenSerializer
    
    def get_queryset(self):
        name = self.kwargs['name']
        password = self.kwargs['password']

        match = Citizen.objects.filter(name=name)
        if (match[0].password == password):
            return match
    
class CitizenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

class ProjectList(generics.ListCreateAPIView):
    search_fields = ['name', 'header', 'description', 'creator__name']
    filter_backends = (filters.SearchFilter,)
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectData(generics.ListAPIView):
    serializer_class = DataEntrySerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return DataEntry.objects.filter(project=id)

class DataList(generics.ListCreateAPIView):
    queryset = DataEntry.objects.all()
    serializer_class = DataEntrySerializer

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataEntry.objects.all()
    serializer_class = DataEntrySerializer

class FormList(generics.ListCreateAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class FormDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Form.objects.all()
    serializer_class = FormSerializer

class FormGrab(generics.ListAPIView):
    serializer_class = FormSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Form.objects.filter(project=id)

class DataVisList(generics.ListCreateAPIView):
    queryset = DataVis.objects.all()
    serializer_class = DataVisSerializer

class DataVisDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataVis.objects.all()
    serializer_class = DataVisSerializer

class ProjectDataVis(generics.ListAPIView):
    serializer_class = DataVisSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return DataVis.objects.filter(project=id)

class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ProjectPosts(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Post.objects.filter(project=id, pinned=False)

class PinnedProjectPosts(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return Post.objects.filter(project=id, pinned=True)