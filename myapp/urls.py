from django.urls import path
from . import views

urlpatterns = [
    path('', views.projects, name='index'),
    path('<int:project_id>/', views.tasks, name='tasks'),
    path('task/<int:task_id>', views.functions, name='functions')
    
]