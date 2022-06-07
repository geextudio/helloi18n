"""helloi18n URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
    
django.conf.urls.url() was deprecated in Django 3.0, and is removed in Django 4.0+
"""
from django.urls import re_path, include
from django.contrib import admin
from django.urls import path

from rest_framework import routers
from helloi18n.helloapi import views as api_views
from projectmanager import views as projects_views

router = routers.DefaultRouter()
router.register(r'users', api_views.UserViewSet)
router.register(r'groups', api_views.GroupViewSet)
router.register(r'projects', api_views.ProjectViewSet)

# route path is usually ended with '/'
urlpatterns = [

    #re_path(r'^', include('projectmanager.urls')),
    # if defined route in app, we can use include('appname.urls') to load the route definitions
    path('', include('projectmanager.urls')),
    # second parameter is ussually defined in app's view
    # app's url should be defined inside app's urls
    # path('projects/', projects_views.project_list, name='projects_home'),

    path('api/', include(router.urls)),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]
