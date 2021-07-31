from django.forms import ModelForm, TextInput, Textarea
from .models import Task, Category


# Model form for create a task
class TaskCreationForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['complete', 'created', ]

        # adding some bootstrap classes and placeholder by widgets
        widgets = {
            'title': TextInput(attrs={'class': 'form-control m-1',
                                      'placeholder': 'Title ...'}),
            'description': Textarea(attrs={'class': 'form-control m-1', 'rows': 3,
                                           'placeholder': 'Description ...'}),
        }
        labels = {key: '' for key in ['title', 'description']}  # removing the labels of title and description


# Model form for update a task
class TaskChangeForm(ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        exclude = ['created', ]
        widgets = {
            'title': TextInput(attrs={'class': 'form-control m-1',
                                      'placeholder': 'Title ...'}),
            'description': Textarea(attrs={'class': 'form-control m-1', 'rows': 5,
                                           'placeholder': 'Description ...'}),
        }
        labels = {key: '' for key in ['title', 'description']}  # removing the labels of title and description


# Model form for create a category
class CategoryCreationForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control m-1',
                                     'placeholder': 'Name ...'}),
        }
        labels = {'name': ''}  # removing the name label
