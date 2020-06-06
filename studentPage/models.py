from django.db import models

# Create your models here.


class Doubts(models.Model):
    sender=models.CharField(max_length=40)
    message=models.CharField(max_length=300)
    receiver=models.CharField(max_length=40)
    course=models.CharField(max_length=40)
    done= models.BooleanField(default=False)