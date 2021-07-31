from django.contrib import admin
from .models import Task, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_filter = ['name']
    search_fields = ['name']
    list_display_links = ['name']
    prepopulated_fields = {'slug': ('name', )}


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'priority', 'category', 'due_date', 'complete']
    list_editable = ['priority', 'category', 'complete']
    list_display_links = ['title']
    search_fields = ['title']
