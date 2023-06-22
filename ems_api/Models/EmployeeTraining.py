from django.db import models
from ems_api.Models.Employee import Employee
from ems_api.Models.Training import Training
class EmployeeTraining(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    poc = models.ForeignKey(Training, on_delete=models.CASCADE)