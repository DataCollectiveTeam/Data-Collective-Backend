from django.db.models import manager
from rest_framework import filters, generics
from .models import Citizen, Project, Form, DataEntry, DataVis
from .serializers import CitizenSerializer, ProjectSerializer, FormSerializer, DataEntrySerializer, DataVisSerializer

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

        #  const closeMatch = { "$regex": searchTerm, "$options": "i" };
        #Post.find( { $or:[ 
        #  {'username':closeMatch},
        #  {'title':closeMatch}, 
        #  {'tags':{$in: [searchTerm]}}, 
        #  { "body":closeMatch}
        #]})
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

class DataVisList(generics.ListAPIView):
    queryset = DataVis.objects.all()
    serializer_class = DataVisSerializer

class DataVisDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DataVis.objects.all()
    serializer_class = DataVisSerializer