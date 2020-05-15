from django.db import models
from django.utils import timezone


class ToDo(models.Model):
    Task = models.TextField( max_length=200 )
    created = models.DateTimeField(default=timezone.now)
    tasktime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
