# Generated by Django 4.1 on 2022-08-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uljesaKojadinovic', '0008_libraryuser_active_member_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowbook',
            name='days_left',
            field=models.IntegerField(default=15, verbose_name='days_left'),
        ),
        migrations.AddField(
            model_name='borrowbook',
            name='returned',
            field=models.BooleanField(default=False),
        ),
    ]
