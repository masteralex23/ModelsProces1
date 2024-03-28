from django.http import HttpResponse, JsonResponse
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.urls import reverse

# Create your views here.

def projects(request):
    projects = Project.objects.all()
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ProjectForm()
    return render(request, 'index.html', {'projects':projects, 'form':form})

def tasks(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    tasks = Task.objects.filter(project=project_id)
    workers = Worker.objects.filter(project=project_id)
    if request.method == 'POST':
        if 'create_task'  in request.POST:
            form = TaskForm(request.POST)
            if form.is_valid():
                form.save()
                url = reverse('tasks', kwargs={'project_id':project_id})
                return redirect(url)
        if 'create_worker' in request.POST:
            form = WorkerForm(request.POST)
            if form.is_valid():
                form.save()
                url = reverse('tasks', kwargs={'project_id':project_id})
                return redirect(url)
    else:
        form_task = TaskForm()
        form_worker = WorkerForm()
    return render(request, 'project.html', {'project': project, 'tasks':tasks, 'workers':workers, 'form_task':form_task, 'form_worker':form_worker})

def functions(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    
    project = task.project
    functions = function.objects.filter(task=task_id)
    workers = Worker.objects.all()
    if request.method == 'POST':
        form = FunctionForm(request.POST)
        if form.is_valid():
            form.save()
            url = reverse('functions', kwargs={'task_id':task_id})
            return redirect(url)
    else:
        form = FunctionForm()
    return render(request, 'task.html', {'task':task, 'functions':functions, 'workers':workers, 'form':form, 'project':project})