from tokenize import Name
from django.db import models

# Create your models here.
class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=20)
    product_description = models.CharField(max_length=50)
    city = models.CharField(max_length=20, default=None,blank= True,null=True)
    state= models.CharField(max_length=20, default=None,blank= True,null=True)

    def __str__(self):
        return str(self.id)+" "+self.name