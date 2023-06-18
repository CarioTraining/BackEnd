from django.db import models

# Create your models here.
    

class Car(models.Model):
    Id = models.AutoField(primary_key=True)
    Price = models.DecimalField(max_digits=12, decimal_places=3, null=True)
    Brand = models.CharField(max_length=50, null=True)
    Model = models.CharField(max_length=50, null=True)
    cc = models.IntegerField(null=True)
    Transmission = models.CharField(max_length=50, null=True)
    Fuel = models.IntegerField(null=True)
    Car_class = models.CharField(max_length=50, null=True)
    Hp = models.IntegerField(max_length=5,null=True)
    Year = models.IntegerField(max_length=4,null=True)
    Photos = models.TextField(null=True)