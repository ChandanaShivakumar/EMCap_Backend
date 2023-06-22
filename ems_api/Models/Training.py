from django.db import models
from ems_api.Models.Employee import Employee

class Training(models.Model):
    
    name = models.CharField(max_length=55 )
    details = models.CharField(max_length=100 )
    start_date= models.DateField()
    end_date= models.DateField()
    employee_id =models.ForeignKey(Employee,on_delete=models.CASCADE, blank=True ,null=True)
    