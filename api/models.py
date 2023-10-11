from django.db import models
from login.models import UserData
# Create your models here.


class Todo(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField(blank=True)
    date = models.DateField(blank=False, auto_now_add=True)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(to=UserData, default=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.Title
