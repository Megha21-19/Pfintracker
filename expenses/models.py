
# expenses/models.py
from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    pass
class Expense(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='expenses/images/') 