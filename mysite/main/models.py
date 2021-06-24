from django.db import models


# Create your models here.
class Contact(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=10)
    username = models.CharField(max_length=64)
    url = models.URLField(max_length=200)


    def __str__(self):
        return self.name
    