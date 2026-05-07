# Generated migration for octofit_tracker with flat MongoDB models

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.FloatField(help_text='Duration in minutes')),
            ],
            options={
                'db_table': 'workouts',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('members', models.JSONField(default=list)),
            ],
            options={
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='Leaderboard',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('score', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'leaderboard',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('activity_type', models.CharField(max_length=100)),
                ('duration', models.FloatField(help_text='Duration in minutes')),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'activities',
            },
        ),
    ]
