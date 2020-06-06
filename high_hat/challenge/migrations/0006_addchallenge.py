# Generated by Django 3.0.6 on 2020-05-30 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenge', '0005_challenge_writer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addchallenge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=200, null=True)),
                ('music', models.CharField(max_length=1000, null=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]