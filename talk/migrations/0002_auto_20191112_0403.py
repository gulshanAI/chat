# Generated by Django 2.2.7 on 2019-11-12 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baatkare',
            name='oppsbot',
            field=models.IntegerField(),
        ),
    ]