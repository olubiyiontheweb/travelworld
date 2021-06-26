from django.db import models
from django_countries.fields import CountryField

# Create your models here.


class Hotel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    price = models.FloatField(max_length=200)
    address1 = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200)
    country = CountryField()
