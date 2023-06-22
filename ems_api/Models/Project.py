from django.db import models
from ems_api.Models.Employee import Employee

class Project(models.Model):
    name = models.CharField(max_length=255)
    manager_name = models.CharField(max_length=255)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE , blank=True, null=True)
    
