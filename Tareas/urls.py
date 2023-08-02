from django.urls import path
from . import views

urlpatterns = [
    path('project/', views.Hello),
    path('projects/', views.Project),
    path('tasks/', views.Task),
    path('newtask/', views.NewTask)
]