from rest_framework import generics
from .models import Citizen, Project, Form, DataEntry
from .serializers import CitizenSerializer, ProjectSerializer, FormSerializer, DataEntrySerializer

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
        return Project.objects.filter(contributor_list__in=id)

class CitizenLogin(generics.ListAPIView):
    serializer_class = CitizenSerializer
    def get_queryset(self):
        username = self.kwargs['username']
        return Citizen.objects.filter(name=username)
    
class CitizenDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citizen.objects.all()
    serializer_class = CitizenSerializer

class ProjectList(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

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
