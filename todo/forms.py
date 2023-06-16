from django import forms

from todo.models import ToDo


class TaskForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('text', 'deadline', 'user')

