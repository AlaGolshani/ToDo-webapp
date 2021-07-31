from django.urls import reverse
from .manager import *


# Category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    objects = CategoryManager()  # The default manager

    def __str__(self):
        return self.name


# Task model
class Task(models.Model):
    PRIORITIES = (
        ('H', 'High'),
        ('M', 'Middle'),
        ('L', 'Low')
    )

    class Meta:
        ordering = ['due_date']

    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, blank=True)
    complete = models.BooleanField(default=False)
    priority = models.CharField(
        max_length=1,
        choices=PRIORITIES,
        default=PRIORITIES[2][0])
    category = models.ForeignKey(Category,
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True,
                                 related_name='tasks')
    due_date = models.DateTimeField(blank=True, null=True)  # expiration datetime of the task
    created = models.DateTimeField(auto_now_add=True)
    objects = TaskManager()  # The default manager

    def get_absolute_url(self):
        return reverse('task-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
