from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

class Manager(models.Model):
    name=models.CharField(max_length=26)
    image=models.ImageField(upload_to='images/')
    
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
