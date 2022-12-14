from django.db import models

# Create your models here.
class Members(models.Model):
    firstname= models.CharField(max_length=255)
    lastname =models.CharField(max_length=255)

class Person(models.Model):
    first_name = models.CharField(max_length = 35)
    last_name = models.CharField(max_length = 35)