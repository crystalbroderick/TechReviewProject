# Generated by Django 2.0.13 on 2019-06-13 20:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gametitle', models.CharField(max_length=255)),
                ('releasedate', models.DateField()),
                ('gamerating', models.CharField(max_length=25)),
                ('genre', models.CharField(max_length=255)),
                ('developer', models.CharField(max_length=255)),
                ('players', models.CharField(max_length=255)),
                ('summary', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'games',
                'db_table': 'game',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewtitle', models.CharField(max_length=255)),
                ('reviewdate', models.DateField()),
                ('reviewrating', models.SmallIntegerField()),
                ('reviewtext', models.TextField()),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='gamereviewapp.Game')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'reviews',
                'db_table': 'review',
            },
        ),
    ]
