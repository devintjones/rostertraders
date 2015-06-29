# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(null=True, blank=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(unique=True, max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pf',
            fields=[
                ('shares', models.IntegerField(db_column='shares')),
                ('id', models.CharField(max_length=20, serialize=False, primary_key=True)),
            ],
            options={
                'db_table': 'PF',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Players',
            fields=[
                ('pid', models.CharField(max_length=20, serialize=False, primary_key=True, db_column='PID')),
                ('name', models.CharField(max_length=255, null=True, db_column='NAME', blank=True)),
                ('team', models.CharField(max_length=255, null=True, db_column='TEAM', blank=True)),
            ],
            options={
                'db_table': 'PLAYERS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gameid', models.CharField(max_length=20, null=True, db_column='gameid', blank=True)),
                ('points', models.IntegerField(null=True, db_column='POINTS', blank=True)),
                ('steals', models.IntegerField(null=True, db_column='STEALS', blank=True)),
                ('rebounds', models.IntegerField(null=True, db_column='REBOUNDS', blank=True)),
                ('assists', models.IntegerField(null=True, db_column='ASSISTS', blank=True)),
            ],
            options={
                'db_table': 'STATS',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PfValue',
            fields=[
                ('user', models.ForeignKey(primary_key=True, db_column='user', serialize=False, to='dashboard.AuthUser')),
                ('cash', models.FloatField(db_column='cash')),
            ],
            options={
                'db_table': 'PF_VALUE',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlayerVals',
            fields=[
                ('pid', models.ForeignKey(primary_key=True, db_column='PID', serialize=False, to='dashboard.Players')),
                ('value', models.FloatField(null=True, db_column='VALUE', blank=True)),
            ],
            options={
                'db_table': 'PLAYER_VALS',
                'managed': False,
            },
        ),
    ]
