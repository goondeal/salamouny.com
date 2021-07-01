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
    


class ProjectType(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)


    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False, null=False)
    desc = models.TextField(blank=True, null=True)
    src_code_url = models.URLField( max_length=200, blank=True, null=True)
    img = models.ImageField(upload_to='images/')
    type = models.ForeignKey(ProjectType, on_delete=models.PROTECT, null=True)


    def __str__(self):
        return self.name