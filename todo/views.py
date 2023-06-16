from django.shortcuts import render

from todo.forms import TaskForm
from todo.models import ToDo


# Create your views here.
def tasks_list(request):
    tasks = ToDo.objects.filter(user=request.user)
    task_form = TaskForm(initial={'user': request.user})
    context = {'title': 'Список задач', 'form': task_form, 'tasks': tasks}
    return render(request, 'todo/todo.html', context=context)


def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            task = form.save()
            context = {'task': task}
            return render(request, 'todo/inc/tasks_list.html', context)

