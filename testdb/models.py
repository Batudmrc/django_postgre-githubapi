from django.db import models

# Create your models here.


class Users(models.Model):
    username = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    Repos = models.IntegerField()

    def __str__(self):
        return self.username

 