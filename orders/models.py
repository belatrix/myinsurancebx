from time import time

from django.db import models


class Order(models.Model):
    car_model = models.CharField(max_length=255)
    created_by = models.ForeignKey('users.User', on_delete=models.PROTECT)
    plate_number = models.CharField(max_length=20)
    accident_location = models.CharField(max_length=255)
    client = models.CharField(max_length=255)


def myinsurance_filename(instance, filename):
    timestamp = int(time())
    return 'myinsurance_folder/%s%d' % (instance, timestamp)


class Attachment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    file = models.FileField(upload_to=myinsurance_filename, null=True, blank=True)
