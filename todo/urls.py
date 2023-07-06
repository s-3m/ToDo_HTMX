from django.urls import path, include

from todo.views import tasks_list, add_task, delete_task, task_finish_update, task_form_update, task_all_update, \
    get_filter_data

urlpatterns = [
    path('list/', tasks_list, name='tasks_list'),
]

HTMX_urls = [
    path('add/', add_task, name='add_task'),
    path('delete/<int:pk>', delete_task, name='delete_task'),
    path('update_finished/<int:pk>', task_finish_update, name='task_finish_update'),
    path('form_update/<int:pk>', task_form_update, name='task_form_update'),
    path('update_task/<int:pk>', task_all_update, name='task_update'),
    path('filter/', get_filter_data, name='filter'),

]

urlpatterns += HTMX_urls
