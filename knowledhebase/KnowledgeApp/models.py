from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Article(models.Model):
    author=models.CharField(max_length=30)
    title=models.CharField(max_length=300)
    text=models.CharField(max_length=3000)
    created_at=models.DateField(default=datetime.now, blank=True)




