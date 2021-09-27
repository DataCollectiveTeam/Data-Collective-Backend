from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view(), name='project_list'),
    path('projects/<int:pk>', views.ProjectDetail.as_view(), name='project_detail'),
    
    path('alist/<str:id>', views.AList.as_view(), name='admin_list'),
    path('contributions/<str:id>', views.Contributions.as_view(), name='contributions'),
    
    path('citizens/', views.CitizenList.as_view(), name='citizen_list'),
    path('citizens/<int:pk>', views.CitizenDetail.as_view(), name='citizen_detail'),
    path('citizens/login/<str:name>&<str:password>', views.CitizenLogin.as_view(), name='citizen_login'),
    
    path('project_data/<int:id>', views.ProjectData.as_view(), name='project_data'),

    path('data_entries/', views.DataList.as_view(), name='data_list'),
    path('data_entries/<int:pk>', views.DataDetail.as_view(), name='data_detail'),
    
    path('forms/', views.FormList.as_view(), name='form_list'),
    path('forms/<int:pk>', views.FormDetail.as_view(), name='form_detail'),
    path('formgrab/<str:id>', views.FormGrab.as_view(), name='form_grab'),

    path('data_vis/', views.DataVisList.as_view(), name='data_vis_list'),
    path('data_vis/<int:pk>', views.DataVisDetail.as_view(), name='data_vis_detail'),    
]