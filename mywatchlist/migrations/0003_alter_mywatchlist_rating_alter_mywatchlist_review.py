# Generated by Django 4.1 on 2022-09-21 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mywatchlist', '0002_mywatchlist_rating_mywatchlist_release_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywatchlist',
            name='rating',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='mywatchlist',
            name='review',
            field=models.TextField(null=True),
        ),
    ]
