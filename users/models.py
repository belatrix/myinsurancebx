from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_inspector = models.BooleanField(default=False)
    is_from_insurance = models.BooleanField(default=False)
    is_from_auto_repair_shop = models.BooleanField(default=False)
    pass
