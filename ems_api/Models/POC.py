from django.db import models
from ems_api.Models.Employee import Employee

class POC(models.Model):
    poc_name = models.CharField(max_length=255 )
    poc_details = models.CharField(max_length=255)
    employee_id=models.ForeignKey(Employee,on_delete=models.CASCADE, blank=True, null=True)
    
    