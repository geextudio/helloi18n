from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from projectmanager.models import Project
from projectmanager.models import TECH_STACK_OPTIONS
# Create your views here.


def project_list(request):
    template = loader.get_template('projectlist.html')
    projects = Project.objects.order_by('name')
    for project in projects:
        project.tech_stack_name = TECH_STACK_OPTIONS[project.tech_stack][1]

    context = {
        'projects': projects,
        'tech_stack_options': TECH_STACK_OPTIONS,
    }
    return HttpResponse(template.render(context, request))
