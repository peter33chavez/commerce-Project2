# Generated by Django 3.1.5 on 2021-03-03 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auctionlistings_startingprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingscomments',
            name='listing_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionlistings'),
        ),
    ]
