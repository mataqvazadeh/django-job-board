from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    location = models.CharField(max_length=100)
    is_remote = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
