from django.db import models
from django.contrib.auth.models import User

class StoreManager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=200,null=True)
    storename = models.CharField(max_length=200,null=True)
    username = models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)
    whatsapp = models.IntegerField(null=True)

    def __str__(self):
        return self.storename
