from django.db import models

# Store Manager - CRUD - Products
class StoreManager(models.Model):
    name = models.CharField(max_length=200, null=True)
    storename = models.CharField(max_length=200)
    whatsapp = models.CharField(max_length=15)

    def __str__(self):
        return self.storename
