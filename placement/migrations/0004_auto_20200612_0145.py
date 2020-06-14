# Generated by Django 2.2.5 on 2020-06-11 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placement', '0003_companydatabase_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='companydatabase',
            old_name='date',
            new_name='date_of_visit',
        ),
        migrations.AddField(
            model_name='companydatabase',
            name='base',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='companydatabase',
            name='cgpa',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='companydatabase',
            name='open_true',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='companydatabase',
            name='total_offers',
            field=models.IntegerField(default=0),
        ),
    ]