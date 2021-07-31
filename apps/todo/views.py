import json
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.views import View
from .forms import *


class TaskList(ListView):
    model = Task
    template_name = 'todo/task_list.html'


class TaskCreateView(CreateView):
    form_class = TaskCreationForm
    template_name = 'todo/add_task.html'
    success_url = reverse_lazy('task-list')


class CategoryList(ListView):
    model = Category
    template_name = 'todo/category_list.html'
    context_object_name = 'categories'

    def get_queryset(self):
        queryset = {
            'full': Category.objects.full_categories(),
            'empty': Category.objects.empty_categories(),
        }
        return queryset


class CategoryCreateView(CreateView):
    form_class = CategoryCreationForm
    template_name = 'todo/add_category.html'
    success_url = reverse_lazy('category-list')


class CategoryTasks(View):
    def get(self, request, slug):
        tasks = Category.objects.get(slug=slug).tasks.all()
        category = Category.objects.get(slug=slug).name
        context = {'tasks': tasks, 'category': category}
        return render(request, 'todo/category_tasks.html', context)


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'


class JsonTasks(View):
    def get(self, request):
        tasks_json = json.loads(serializers.serialize("json", Task.objects.all()))
        data = {"tasks": tasks_json}
        return JsonResponse(data, json_dumps_params={'indent': 4})


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskChangeForm
    template_name_suffix = '_edit'


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy('task-list')


class CategoryUpdateView(UpdateView):
    model = Category
    form_class = CategoryChangeForm
    template_name_suffix = '_edit'


class CategoryDeleteView(DeleteView):
    model = Category
    success_url = reverse_lazy('category-list')
