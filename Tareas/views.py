from django.shortcuts import render
# Create your views here.
def Hello(Request):
    return render(Request, "Project.html")

def Project(request):
    projects = projects.objects.all()
    return render(request, 'projects.html',{'projects':projects})