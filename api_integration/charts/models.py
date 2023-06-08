from django.db import models

# Create your models here.
class Product(models.Model):
    productID=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    price=models.FloatField()
    description=models.TextField()
    
