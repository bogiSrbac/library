# Generated by Django 4.0.7 on 2022-08-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uljesaKojadinovic', '0011_alter_borrowbook_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryuser',
            name='days_left',
            field=models.IntegerField(blank=True, null=True, verbose_name='days_left'),
        ),
    ]