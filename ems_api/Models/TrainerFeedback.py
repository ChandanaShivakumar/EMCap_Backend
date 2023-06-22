from django.db import models
from ems_api.Models.Trainer import Trainer
from ems_api.Models.Employee import Employee


class TrainerFeedback(models.Model):
    fresher_id=models.ForeignKey(Employee, on_delete=models.CASCADE)
    triner_id=models.ForeignKey(Trainer, on_delete=models.CASCADE)
    feeback=models.TextField()
    reply =models.CharField(max_length=26)