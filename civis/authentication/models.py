from django.db import models

# Create your models here.
class Policy(models.Model):
    name = models.CharField(max_length=120)
    desc = models.TextField(default='SOME STRING')
 
    def __str__(self):
        return self.name

class Feedback(models.Model):
    policy = models.CharField(max_length=120)
    answer = models.TextField(blank=True, null=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='None')
    age = models.IntegerField(default='None')
    STATE_CHOICES = (
    ("Andhra","Andhra"),
    ("Telangana","Telangana"),
    ("West Bengal","West Bengal"),
    ("Assam","Assam"),
    ("Bihar","Bihar"),
    ("Goa","Goa"),
    ("Chattisghar","Chattisghar"),
    ("Gujarat","Gujarat"),
    ("Haryana","Haryana"),
    ("J & K","J & K"),
    ("Jharkhand","Jharkhand"),
    ("Madhya Pradesh","Madhya Pradesh"),
    ("Kerala","Kerala"),

    )
    location = models.CharField(max_length=20, choices=STATE_CHOICES,default='None')
    RATING_CHOICES = (
        ('3', '3'),
        ('2', '2'),
        ('1','1')
    )
    rating = models.CharField(max_length=2, choices=RATING_CHOICES,default='None')
 
    def __str__(self):
        return self.answer

    class Meta:
        db_table = "authentication_feedback"

