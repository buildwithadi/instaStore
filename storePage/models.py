from django.db import models

# Create your models here.
class Product(models.Model):
    pName = models.CharField(max_length=200,null=True)
    pDescription = models.TextField(null=True)
    pPrice = models.IntegerField(null=True)
    pImage = models.ImageField(upload_to='product_images/', null=True, blank=True)

    def __str__(self):
        return self.pName