from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    is_teacher = models.BooleanField("Is teacher",default = False)
    is_student = models.BooleanField("Is student",default = False)
