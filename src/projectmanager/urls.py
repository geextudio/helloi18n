from django.urls import re_path, path
from projectmanager import views

urlpatterns = [
    path('projects', views.project_list, name='default_project_list'),
    path('projects/<int:project_id>/',
         views.project_detail, name='project_detail'),
    #re_path(r'^projectlist', views.project_list, name='project_list'),
]
