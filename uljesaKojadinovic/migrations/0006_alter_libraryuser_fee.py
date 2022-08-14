# Generated by Django 4.1 on 2022-08-07 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uljesaKojadinovic', '0005_libraryuser_duration_libraryuser_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libraryuser',
            name='fee',
            field=models.DecimalField(choices=[(0.0, '0.00'), (10.0, '1.00'), (20.0, '20.00'), (30.0, '30.00'), (40.0, '40.00'), (50.0, '50.00')], decimal_places=2, default=0.0, max_digits=4, verbose_name='fee'),
        ),
    ]