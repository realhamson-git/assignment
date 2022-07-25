from django.db import models
from django.contrib.auth.models import User

# Create your models here.
typeChoises = (('patient','patient'),('doctor','doctor'))
class extendUser(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    address = models.CharField(max_length = 1000)
    profile = models.ImageField(upload_to = 'profile/')
    types = models.CharField(choices = typeChoises, max_length = 10)

