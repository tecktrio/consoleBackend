from django.db import models

# Create your models here.

class Products(models.Model):
    Name = models.CharField(max_length=50,default='None')
    Icon = models.ImageField(upload_to='Product_Icons')
    ImageA = models.ImageField(upload_to='Product_Images_A')
    ImageB = models.ImageField(upload_to='Product_Images_A')
    ImageC = models.ImageField(upload_to='Product_Images_A')
    ImageD = models.ImageField(upload_to='Product_Images_D')
    Description = models.CharField(max_length=200,default='None')
    DownloadLink = models.CharField(max_length=200,default='None')
    Installs = models.CharField(max_length=50,default='None')
    Documentation = models.CharField(max_length=200,default='None')
    
    def __str__(self):
        return self.Name
    