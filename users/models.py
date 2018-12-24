from django.db import models
from django.contrib.auth.models import AbstractUser


class Role(models.Model):
    name = models.CharField(max_length=100)

    class Meta(object):
        ordering = ['name']

    def __str__(self):
        return self.name


class User(AbstractUser):
    role = models.ForeignKey(Role, blank=True, null=True, on_delete=models.CASCADE)
    pass
