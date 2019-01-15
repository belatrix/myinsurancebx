from requests import get as requests_get

from django.db.models.signals import post_save
from django.dispatch import receiver
from eth_hash.auto import keccak

from .models import Attachment


@receiver(post_save, sender=Attachment)
def create_attachment(sender, instance, created, **kwargs):
    if created:
        response = requests_get(instance.file.url)
        file = response.content
        hash = keccak.new(file)
        print(hash.digest().hex())
