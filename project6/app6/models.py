from django.db import models

class registration(models.Model):

    name = models.CharField(max_length=50)
    contact = models.IntegerField()
    email = models.EmailField(max_length=100,unique=True)
    password = models.CharField(max_length=10)
    location = models.CharField(max_length=50)


