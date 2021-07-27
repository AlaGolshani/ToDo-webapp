from django.db import models
from datetime import datetime
from django.db.models import Count
from django.urls import reverse


class CategoryManager(models.Manager):
    def no_task(self):
        return self.annotate(num_task=Count('tasks')).filter(num_task=0)

    def has_task(self):
        return self.annotate(num_task=Count('tasks')).filter(num_task__gt=0)


class Category(models.Model):
    name = models.CharField(max_length=100)
    objects = CategoryManager()

    def __str__(self):
        return self.name


class TaskManager(models.Manager):
    def expired_tasks(self):
        return self.filter(deadline__lt=datetime.now())


class Task(models.Model):
    PRIORITIES = (
        ('H', 'High'),
        ('M', 'Medium'),
        ('L', 'Low')
    )

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITIES,
        default=PRIORITIES[2][0]
    )
    complete = models.BooleanField(default=False)
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True,
                                 related_name='tasks')
    deadline = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = TaskManager()

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
