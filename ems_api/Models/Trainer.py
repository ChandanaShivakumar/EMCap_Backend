from django.db import models

class Trainer(models.Model):
    name= models.CharField(max_length=24)
    image=models.ImageField()
    employee_id=models.BigIntegerField()
    triner_id=models.IntegerField(primary_key=True)
    