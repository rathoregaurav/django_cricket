# Generated by Django 2.2.5 on 2020-06-27 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
                ('short_name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'country',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(db_index=True, max_length=100)),
                ('logo_uri', models.URLField()),
                ('point', models.PositiveSmallIntegerField(default=0)),
                ('club_state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='team.Country')),
            ],
            options={
                'db_table': 'cricket_teams',
            },
        ),
    ]
