from django.conf import settings
from django.db import models
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser

from rest_framework.authtoken.models import Token


class User(AbstractUser):
    is_inspector = models.BooleanField(default=False)
    is_from_insurance = models.BooleanField(default=False)
    is_from_auto_repair_shop = models.BooleanField(default=False)
    pass


@receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
