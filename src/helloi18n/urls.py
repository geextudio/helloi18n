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
from helloi18n.helloapi import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'projects', views.ProjectViewSet)

urlpatterns = [

    #re_path(r'^', include('projectmanager.urls')),
    path('', include('projectmanager.urls')),

    path('api/', include(router.urls)),
    path('api-auth/',
         include('rest_framework.urls', namespace='rest_framework')),

    path('admin/', admin.site.urls),
]
