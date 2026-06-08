from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=100)
    
class Region(models.Model):
    name=models.CharField(max_length=100)
    country = models.ForeignKey(Country,  on_delete=models.CASCADE)
class City(models.Model):
    name=models.CharField(max_length=100)
    region = models.ForeignKey(Region,  on_delete=models.CASCADE)
class Customers(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    cellphone=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    city= models.ForeignKey(City, on_delete=models.CASCADE)  
       