# Generated by Django 3.0.8 on 2020-08-03 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photohub', '0002_auto_20200803_0916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='image',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='location',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
