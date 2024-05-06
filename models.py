from django.db import models

# Create your models here.

class User(models.Model):
    def __str__(self):
        return self.name
    user_name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=50)
    otp=models.CharField(max_length=10,default=" ")
    is_verified=models.IntegerField(default=0)
  
class Url(models.Model):
    long_url=models.CharField(max_length=100)
    short_url=models.CharField(max_length=20)  
    user_id=models.IntegerField()  