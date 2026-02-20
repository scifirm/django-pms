from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ActivityLog(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        action = models.CharField(max_length=255)
        timestamp = models.DateTimeField(auto_now_add=True)

        def __str__(self):
         return f"{self.user} - {self.action}"