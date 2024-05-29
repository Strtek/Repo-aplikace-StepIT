from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

