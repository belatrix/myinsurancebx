# Generated by Django 2.1.5 on 2019-01-29 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AutoRepairShop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'auto repair shop',
                'verbose_name_plural': 'auto repair shops',
            },
        ),
    ]
