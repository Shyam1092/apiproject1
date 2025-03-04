from django.db import models

# Create your models here.

class todo(models.Model):
    titel=models.CharField(max_length=50)
    completed=models.CharField(max_length=20)