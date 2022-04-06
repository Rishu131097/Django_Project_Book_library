from django.db import models

# Create your models here.
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    publisher = models.CharField(max_length=20)
    privilege = models.CharField(max_length=50)
    city = models.CharField(max_length=20, default=None,blank= True,null=True)
    state= models.CharField(max_length=20, default=None,blank= True,null=True)

    def __str__(self):
         return str(self.id)+" "+self.title