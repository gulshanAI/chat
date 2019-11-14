# Generated by Django 2.2.7 on 2019-11-12 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('talk', '0004_baatkare_reply'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baatkare',
            name='reply',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='for_reply', to=settings.AUTH_USER_MODEL),
        ),
    ]