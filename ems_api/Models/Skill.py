from django.db import models
from ems_api.Models.Employee import Employee
class Skill(models.Model):
    name     =models.CharField(max_length= 30)
    details  =models.TextField(max_length=100)
    emp_id  =models.ForeignKey(Employee,on_delete=models.CASCADE, blank=True, null=True)