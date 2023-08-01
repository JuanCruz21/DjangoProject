from django.shortcuts import render
from .models import Projects,Tasks
# Create your views here.
def Hello(Request):
    return render(Request, "Project.html")

def Project(request):
    projects = Projects.objects.all()
    return render(request, 'Projects.html',{
        'projects':projects
    })