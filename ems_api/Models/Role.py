from django.db import models

class Role(models.Model):
    roll_id=models.IntegerField(primary_key=True)
    roll_name=models.CharField(max_length=15)
    