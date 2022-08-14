# Generated by Django 4.1 on 2022-08-04 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uljesaKojadinovic', '0002_authorbook_book_libraryuser_first_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MembershipFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='start date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end date')),
                ('fee', models.DecimalField(choices=[(10.0, '10.00'), (20.0, '20.00'), (30.0, '30.00'), (40.0, '40.00'), (50.0, '50.00')], decimal_places=2, max_digits=4)),
                ('member', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='member')),
            ],
        ),
    ]
