from django.forms import ModelForm, TextInput, Textarea
from .models import Task, Category


class TaskCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['complete', 'created', ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control m-1'}),
            'description': Textarea(attrs={'class': 'form-control m-1', 'rows': 5}),
        }


class TaskChangeForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created', ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control m-1'}),
            'description': Textarea(attrs={'class': 'form-control m-1', 'rows': 5}),
        }


class CategoryCreationForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control m-1'}),
        }
