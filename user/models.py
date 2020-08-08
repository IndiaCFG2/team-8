from django.db import models

# Create your models here.
class Policy(models.Model):
    name = models.CharField(max_length=120)
    summary = models.TextField()
    # answer = models.TextField()
    def __str__(self):
        return self.name

GENDER_CHOICES = (
    ("male","male"),
    ("female","female"),
    ("other","other")
)

STATE_CHOICE = (
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

class Answer(models.Model):
    question = models.ForeignKey(Policy, on_delete=models.CASCADE)
    answer = models.TextField()
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES,default="male")
    age = models.IntegerField(default=18)
    region = models.CharField(max_length= 30,choices = STATE_CHOICE,default="Telangana")
    def __str__(self):
        return self.answer