# Generated by Django 2.0.7 on 2018-07-10 05:33

import app.models.player
from django.db import migrations, models
import enumfields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20180709_0226'),
    ]

    operations = [
        migrations.AddField(
            model_name='faction',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='signupinvite',
            name='player_role',
            field=enumfields.fields.EnumField(blank=True, enum=app.models.player.PlayerRole, max_length=1, null=True),
        ),
    ]