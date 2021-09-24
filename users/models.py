from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    year = models.PositiveIntegerField(null= False , blank = False , default = '3')
    first_name = models.CharField(max_length= 100)
    last_name = models.CharField(max_length= 100,null= True , blank = True)
    


    
