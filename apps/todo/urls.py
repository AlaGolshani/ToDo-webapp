from django.urls import path
from .views import *

urlpatterns = [
    path('task-list/', TaskList.as_view(), name='task-list'),
    path('add-task/', TaskCreateView.as_view(), name='add-task'),
    path('category-list/', CategoryList.as_view(), name='category-list'),
    path('add-category/', CategoryCreateView.as_view(), name='add-category'),
    path('<int:pk>/category-tasks/', CategoryTasks.as_view(), name='category-tasks'),
    path('<int:pk>/task-detail/', TaskDetailView.as_view(), name='task-detail'),
    path('download-tasks/', JsonTasks.as_view(), name='download-tasks'),
    path('<int:pk>/task-edit/', TaskUpdateView.as_view(), name='task-edit'),
    path('<int:pk>/task-delete/', TaskDeleteView.as_view(), name='task-delete'),
]
