from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=30)
    LEVELS = (('Beginner', 'Beginner'),('Intermediate', 'Intermediate'),('Advanced', 'Advanced'),)
    level = models.CharField(max_length=20,choices=LEVELS)
    description = models.CharField(max_length=150)
    takeaways = models.CharField(max_length=200)
    creator = models.ForeignKey(User ,on_delete=models.CASCADE)
    members=models.ManyToManyField(User,blank=True,related_name="Courses")


class Chats(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    message=models.CharField(max_length=200 ,blank=True)
    image=models.ImageField(blank=True,upload_to='media')
    time=models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.time = timezone.now()
        print(self.time)
        return super(Chats, self).save(*args, **kwargs)

