# Generated by Django 3.1.5 on 2021-03-03 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionlistings',
            name='startingPrice',
            field=models.DecimalField(decimal_places=2, max_digits=10000, null=True),
        ),
    ]
