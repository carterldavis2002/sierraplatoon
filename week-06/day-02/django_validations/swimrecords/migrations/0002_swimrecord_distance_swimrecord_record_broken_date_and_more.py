# Generated by Django 4.1.2 on 2022-11-07 06:32

import datetime
import django.core.validators
from django.db import migrations, models
import django.utils.timezone
import swimrecords.models


class Migration(migrations.Migration):

    dependencies = [
        ('swimrecords', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='swimrecord',
            name='distance',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(50)]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='swimrecord',
            name='record_broken_date',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[django.core.validators.MaxValueValidator(models.DateTimeField(validators=[django.core.validators.MaxValueValidator(datetime.datetime(2022, 11, 7, 6, 31, 24, 786323, tzinfo=datetime.timezone.utc), "Can't set record in the future.")]))]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='swimrecord',
            name='record_date',
            field=models.DateTimeField(default=django.utils.timezone.now, validators=[django.core.validators.MaxValueValidator(datetime.datetime(2022, 11, 7, 6, 31, 24, 786323, tzinfo=datetime.timezone.utc), "Can't set record in the future.")]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='swimrecord',
            name='relay',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='swimrecord',
            name='stroke',
            field=models.CharField(default='', max_length=255, validators=[swimrecords.models.validate_stroke]),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='swimrecord',
            name='team_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]