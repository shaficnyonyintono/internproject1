from django.db import models
from time import timezone
from django.utils import timezone
 
class Register(models.Model):
    age_choices = [
        ('F','Female'),
        ('M','Male')
    ]
    first_name = models.CharField(max_length=100, help_text="Enter your first name")
    last_name = models.CharField(max_length=100, help_text="enter your last name")
    email = models.EmailField(max_length=50,help_text="enter your email address")
    sex = models.CharField(max_length=10, choices=age_choices, default='M')
    def __str__(self):
        return self.first_name
    
    

        

# Create your models here.
