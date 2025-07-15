from django.db import models

# Create your models here.
class Product(models.Model):
    pName = models.CharField(max_length=200)
    pDescription = models.TextField()
    pPrice = models.IntegerField()

    def __str__(self):
        return self.pName