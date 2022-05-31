from django.urls import re_path
from projectmanager import views

urlpatterns = [
    re_path(r'^projectlist', views.project_list, name='project_list'),
]
