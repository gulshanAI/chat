# Generated by Django 2.2.7 on 2019-11-13 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0008_auto_20191112_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baatkare',
            name='msgdate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
