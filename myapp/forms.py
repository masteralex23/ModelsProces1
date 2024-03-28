from django import forms
from .models import *

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name']

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'project']

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'project']

class FunctionForm(forms.ModelForm):
    class Meta:
        model = function
        fields = ['name', 'time_worked', 'task', 'worker']