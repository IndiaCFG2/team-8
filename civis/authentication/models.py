from django.db import models

# Create your models here.
class Policy(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField(default='SOME STRING')
 
    def __str__(self):
        return self.name

class Feedback(models.Model):
    user_name = models.CharField(max_length=120)
    policy = models.TextField()
    gender = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    age = models.TextField()
    happy = models.BooleanField()
    date = models.DateField(auto_now_add=True)
    
 
    def __str__(self):
        return self.user_name

