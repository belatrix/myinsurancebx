from time import time

from django.db import models

from utils.hash import keccak_hash_file


class OrderStatus(models.Model):
    name = models.CharField(max_length=100)
    is_default = models.BooleanField(default=False)
    ordering = models.PositiveIntegerField(default=0)

    class Meta(object):
        verbose_name_plural = 'order statuses'
        ordering = ['ordering']

    def __str__(self):
        return self.name


class AutoRepairShop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    class Meta(object):
        verbose_name = 'auto repair shop'
        verbose_name_plural = 'auto repair shops'

    def __str__(self):
        return self.name


class Order(models.Model):
    car_model = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('users.User', on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    priority = models.PositiveIntegerField(default=1)
    plate_number = models.CharField(max_length=20, blank=True, null=True)
    accident_location = models.CharField(max_length=255, blank=True, null=True)
    client = models.CharField(max_length=255, blank=True, null=True)
    client_policy_number = models.CharField(max_length=10, blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    is_behind_payment = models.BooleanField(blank=True, null=True)
    status = models.ForeignKey(OrderStatus, blank=True, null=True, on_delete=models.PROTECT)
    budget = models.PositiveIntegerField(blank=True, null=True)
    auto_repair_shop = models.ForeignKey(AutoRepairShop,
                                         on_delete=models.PROTECT,
                                         related_name="repairshop_order",
                                         blank=True,
                                         null=True)

    class Meta(object):
        ordering = ['priority', '-id']

    def __str__(self):
        return str(self.id)


def myinsurance_filename(instance, filename):
    timestamp = int(time())
    return 'myinsurance_folder/%d%s' % (timestamp, str(instance))


class Attachment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_attachment")
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
