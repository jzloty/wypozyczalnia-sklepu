# Generated by Django 3.2.2 on 2021-05-29 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gry', '0004_auto_20210529_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nazwagry',
            name='Data_orientacyjny_zwrot',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nazwagry',
            name='Data_wypozyczenie',
            field=models.DateField(blank=True, null=True),
        ),
    ]