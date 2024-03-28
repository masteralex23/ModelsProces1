from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=200)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class Worker(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class function(models.Model):
    name = models.CharField(max_length=200)
    time_worked = models.CharField(max_length=20)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE)