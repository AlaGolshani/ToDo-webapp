from django.contrib import admin

# Register your models here.
from .models import Task, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    list_editable = ['name']
    search_fields = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'priority', 'category', 'due_date', 'complete']
    list_editable = ['title', 'priority', 'category', 'complete']
    search_fields = ['title']
