# Generated by Django 4.1.2 on 2022-11-07 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', through='imdb.Role', to='imdb.actor'),
        ),
        migrations.AlterField(
            model_name='role',
            name='actor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='imdb.actor'),
        ),
        migrations.AlterField(
            model_name='role',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='imdb.movie'),
        ),
    ]
