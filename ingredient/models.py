from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=30)
    img_url = models.CharField(max_length=100)
    quantity = models.IntegerField()