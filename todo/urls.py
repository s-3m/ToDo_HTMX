from django.urls import path, include

from todo.views import tasks_list, add_task

urlpatterns = [
    path('list/', tasks_list, name='tasks_list'),
]

HTMX_urls = [
    path('add/', add_task, name='add_task')
]

urlpatterns += HTMX_urls
