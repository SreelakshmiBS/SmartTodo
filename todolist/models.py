# models.py

from django.db import models
from django.contrib.auth.models import User


class Today_Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    description = models.TextField()

    completed = models.BooleanField(default=False)
    status = models.CharField(max_length=20, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.title


class Reminder(models.Model):

    task = models.ForeignKey(
        Today_Task,
        on_delete=models.CASCADE,
        related_name='reminders'
    )

    reminder_time = models.DateTimeField()

    message = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default='pending')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.message