from django.contrib.auth.models import User
from django.db import models
from chat.models import User

class Student(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True,blank=True)
    first_name =models.CharField(max_length=255,null=True,blank=True)
    last_name =models.CharField(max_length=255,null=True,blank=True)
    age = models.IntegerField(default=0) 
    phone = models.IntegerField(null=True,blank=True)
    joined_date = models.DateField(null=True,blank=True)

