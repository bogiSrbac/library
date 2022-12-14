# Generated by Django 4.1 on 2022-08-07 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uljesaKojadinovic', '0004_alter_borrowbook_book_alter_borrowbook_borrower'),
    ]

    operations = [
        migrations.AddField(
            model_name='libraryuser',
            name='duration',
            field=models.IntegerField(default=0, verbose_name='duration'),
        ),
        migrations.AddField(
            model_name='libraryuser',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='end date'),
        ),
        migrations.AddField(
            model_name='libraryuser',
            name='fee',
            field=models.DecimalField(choices=[(0.0, '00.00'), (10.0, '10.00'), (20.0, '20.00'), (30.0, '30.00'), (40.0, '40.00'), (50.0, '50.00')], decimal_places=2, default=0.0, max_digits=4, verbose_name='fee'),
        ),
        migrations.AddField(
            model_name='libraryuser',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='start date'),
        ),
        migrations.AlterField(
            model_name='libraryuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='MembershipFee',
        ),
    ]
