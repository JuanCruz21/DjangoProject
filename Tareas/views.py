from django.shortcuts import render,redirect
from .models import Projects,Tasks
from .Forms import createnewtask
# Create your views here.
def Hello(Request):
    return render(Request, "Project.html")

def Project(request):
    projects = Projects.objects.all()
    return render(request, 'Projects.html',{
        'projects':projects
    })

def Task(request):
    tasks = Tasks.objects.all()
    return render(request, 'Tasks.html',{
        'tasks':tasks
    })

def NewTask(request):
    if request.method == 'GET':
        return render(request, 'NewTask.html',{
        'form': createnewtask()
        })
    else:
        Tasks.objects.create(name=request.POST['name'],description=request.POST['description'], Projects_id=1)
        return redirect('/tasks/')
    
    
    
