from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.hash import keccak_hash_file_url

from .models import Attachment


@receiver(post_save, sender=Attachment)
def create_attachment(sender, instance, created, **kwargs):
    if created:
        hash = keccak_hash_file_url(instance.file.url)
        Attachment.objects.filter(pk=instance.pk).update(hash=hash)
