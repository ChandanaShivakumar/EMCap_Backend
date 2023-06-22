from django.db import models
from ems_api.Models.Employee import Employee

class Profile(models.Model):
    employee      = models.OneToOneField(Employee, on_delete=models.CASCADE , blank=True)
    phone_number  = models.CharField(max_length=20)
    location       = models.CharField(max_length=100)
    designation   = models.CharField(max_length=100)
    image         = models.ImageField(upload_to='media/images/')