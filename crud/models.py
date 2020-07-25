from django.db import models


# Create your models here.
class PersonInfo(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    # image = models.ImageField(max_length=100)
