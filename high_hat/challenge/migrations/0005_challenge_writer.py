# Generated by Django 3.0.6 on 2020-05-30 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0004_auto_20200530_0447'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='writer',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
