# Generated by Django 3.1.7 on 2021-04-18 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20210314_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionlistings',
            name='description',
            field=models.TextField(max_length=4000, null=True),
        ),
    ]
