from time import time

from django.db import models

from utils.hash import keccak_hash_file


class Order(models.Model):
    car_model = models.CharField(max_length=255)
    created_by = models.ForeignKey('users.User', on_delete=models.PROTECT)
    plate_number = models.CharField(max_length=20)
    accident_location = models.CharField(max_length=255)
    client = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id)


def myinsurance_filename(instance, filename):
    timestamp = int(time())
    return 'myinsurance_folder/%d%s' % (timestamp, str(instance))


class Attachment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    file = models.FileField(upload_to=myinsurance_filename)
    uploaded_by = models.ForeignKey('users.User', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    hash = models.CharField(max_length=64, null=True, blank=True)
    hash_url = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.created_at != self.modified_at:
            self.hash = keccak_hash_file(self.file.read())
        super(Attachment, self).save(*args, **kwargs)

    def __str__(self):
        return self.file.name
