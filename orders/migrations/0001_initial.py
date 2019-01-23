# Generated by Django 2.1.5 on 2019-01-23 02:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import orders.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=orders.models.myinsurance_filename)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('hash', models.CharField(blank=True, max_length=64, null=True)),
                ('hash_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_model', models.CharField(max_length=255)),
                ('plate_number', models.CharField(max_length=20)),
                ('accident_location', models.CharField(max_length=255)),
                ('client', models.CharField(max_length=255)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='attachment',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='orders.Order'),
        ),
        migrations.AddField(
            model_name='attachment',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
