from django.urls import path
from . import views


urlpatterns = [
    path('', views.tasks, name='tasklist'),
    path('<int:pk>', views.EachTask.as_view(), name='task-detail'),
    path('create/', views.tasks, name='task_create')
]
