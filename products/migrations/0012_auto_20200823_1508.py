# Generated by Django 3.0.8 on 2020-08-23 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_auto_20200823_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.IntegerField(null=True),
        ),
    ]
