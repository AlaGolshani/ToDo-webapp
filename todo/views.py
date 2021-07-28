import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView
from django.views import View
from .forms import *


class TaskList(ListView):
    model = Task
    template_name = 'task/task_list.html'
    queryset = Task.objects.all().order_by('due_date')


class TaskCreateView(CreateView):
    form_class = TaskCreationForm
    template_name = 'task/add_task.html'
    success_url = reverse_lazy('task-list')


class CategoryList(ListView):
    model = Category
    template_name = 'task/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = {
            'first': Category.objects.has_task(),
            'last': Category.objects.no_task(),
        }
        return queryset


class CategoryCreateView(CreateView):
    form_class = CategoryCreationForm
    template_name = 'task/add_category.html'
    success_url = reverse_lazy('category-list')


class CategoryTasks(View):
    def get(self, request, pk):
        tasks = Category.objects.get(pk=pk).tasks.all()
        category = Category.objects.get(pk=pk).name
        context = {'tasks': tasks, 'category': category}
        return render(request, 'task/category_tasks.html', context)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'


class JsonTasks(View):
    def get(self, request):
        tasks_json = json.loads(serializers.serialize("json", Task.objects.all()))
        data = {"tasks": tasks_json}
        return JsonResponse(data, json_dumps_params={'indent': 4})
