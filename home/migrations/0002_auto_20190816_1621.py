# Generated by Django 2.2 on 2019-08-16 10:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statistic',
            options={'ordering': ['identifier']},
        ),
    ]
