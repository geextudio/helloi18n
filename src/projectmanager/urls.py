from django.urls import re_path, path
from projectmanager import views

urlpatterns = [
    path('', views.project_list, name='default_project_list'),
    re_path(r'^projectlist', views.project_list, name='project_list'),
]
