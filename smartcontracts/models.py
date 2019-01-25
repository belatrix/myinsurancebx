from django.db import models

class Timestamp(models.Model):
    id = models.IntegerField(primary_key=True)
    file_hash = models.CharField(max_length=64)
    incomplete_timestamp = models.BinaryField()
    complete_timestamp = models.BinaryField()

    class Meta:
        db_table = 'timestamp'

