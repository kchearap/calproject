# Generated by Django 2.0.4 on 2018-05-15 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daycal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='calorie',
            field=models.SmallIntegerField(default=2000, null=True),
        ),
        migrations.AddField(
            model_name='meal',
            name='cal_per_day',
            field=models.SmallIntegerField(default=2000, null=True),
        ),
    ]
