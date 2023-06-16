from django.contrib.auth import get_user_model
from django.db import models


# Create your models here.
class ToDo(models.Model):
    text = models.CharField(null=False, blank=False, max_length=260)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=None, related_name='tasks')
    create_by = models.DateField(auto_now_add=True, blank=True, null=True)
    is_finished = models.BooleanField(default=False, blank=True, null=True)
    deadline = models.DateField(default=None, blank=True, null=True)

    def __str__(self):
        return f'Task - {self.text}'

