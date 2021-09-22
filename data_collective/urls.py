from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('projectss/<int:pk>', views.ProjectDetail.as_view(), name='project_detail'),
    path('citizens/', views.CitizenList.as_view(), name='citizen_list'),
    path('citizens/<int:pk>', views.CitizenDetail.as_view(), name='citizen_detail'),
]