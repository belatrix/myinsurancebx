# Generated by Django 2.1.5 on 2019-02-08 18:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190205_1433'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['priority']},
        ),
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='priority',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
