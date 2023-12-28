from django.db import models

###  WHEN MAKING CHANGES TO models.py, ALWAYS RUN 'python manage.py makemigrations' followed by 'python manage.py migrate'  ###

# Create your models here.
class Product(models.Model):
    title = models.TextField(default='title')
    description = models.TextField(default='description')
    price = models.TextField(default='price')
    summary = models.TextField(default='this is cool!')