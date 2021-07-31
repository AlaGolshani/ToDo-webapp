from django.db.models import Count
from django.db import models
from datetime import datetime


# A model manager for Category
class CategoryManager(models.Manager):

    def empty_categories(self):
        """
        return a queryset of category objects that have no task
        """
        return self.filter(tasks__isnull=True)

    def full_categories(self):
        """
        return a queryset of category objects that have at least one task
        """
        return self.annotate(num_task=Count('tasks')).filter(num_task__gt=0)


# A model manager for Task
class TaskManager(models.Manager):
    def expired_tasks(self):
        """
        return a queryset of task objects that have been expired
        """
        return self.filter(due_date__lt=datetime.now())
