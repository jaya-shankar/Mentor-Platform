from django.db import models
from mentorPage.models import Course
from django.contrib.auth.models import User

# Create your models here.


class Doubts(models.Model):
    sender=models.ForeignKey(User ,on_delete=models.CASCADE ,related_name="sender")
    message=models.CharField(max_length=150)
    receiver=models.ForeignKey(User ,on_delete=models.CASCADE ,related_name="receiver")
    course=models.ForeignKey(Course ,on_delete=models.CASCADE)
    done= models.BooleanField(default=False)