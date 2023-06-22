from django.utils import timezone
from django.db import models
from ems_api.Models.Employee import Employee
from ems_api.Models.Manager import Manager


class Feedback(models.Model):
    fresher_id=models.ForeignKey(Employee, on_delete=models.CASCADE)
    manager_id=models.ForeignKey(Manager, on_delete=models.CASCADE)
    manager_name=models.TextField(max_length=40, default='')
    feedback=models.TextField()
    rating = models.IntegerField( default=1)
    file =models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)