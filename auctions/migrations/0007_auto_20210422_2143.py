# Generated by Django 3.1.7 on 2021-04-22 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auto_20210418_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctionlistings',
            old_name='startingPrice',
            new_name='price',
        ),
    ]