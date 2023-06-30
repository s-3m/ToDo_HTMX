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
            return render(request, 'todo/inc/tasks_item.html', context)


def delete_task(request, pk):
    request.user.tasks.filter(pk=pk).delete()
    tasks = ToDo.objects.filter(user=request.user)
    context = {'tasks': tasks}
    return render(request, 'todo/inc/task_list.html', context=context)


def task_finish_update(request, pk):
    task = ToDo.objects.get(pk=pk)
    if not task.is_finished:
        task.is_finished = True
    else:
        task.is_finished = False
    task.save()

    return render(request, 'todo/inc/tasks_item.html', context={'task': task})


def task_form_update(request, pk):
    task = ToDo.objects.get(pk=pk)
    task_form = TaskForm(initial={'user': request.user, 'text': task.text, 'deadline': task.deadline})
    context = {'form': task_form, 'task': task}
    return render(request, 'todo/inc/task_update.html', context=context)


def task_all_update(request, pk):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        if form.is_valid():
            task = ToDo.objects.get(pk=pk)
            task.text = form.cleaned_data['text']
            task.deadline = form.cleaned_data['deadline']
            task.user = form.cleaned_data['user']
            task.save()
            tasks = request.user.tasks.all()
            return render(request, 'todo/inc/task_list.html', context={'tasks': tasks})
