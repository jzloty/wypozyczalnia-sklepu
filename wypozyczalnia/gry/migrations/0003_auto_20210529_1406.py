# Generated by Django 3.2.2 on 2021-05-29 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gry', '0002_auto_20210526_1457'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nazwagry',
            name='add_date',
        ),
        migrations.AddField(
            model_name='nazwagry',
            name='Data_orientacyjny_zwrot',
            field=models.DateTimeField(null=True, verbose_name='data orientacyjnego zwrotu'),
        ),
        migrations.AddField(
            model_name='nazwagry',
            name='Data_wypozyczenie',
            field=models.DateTimeField(null=True, verbose_name='data wypozyczenia'),
        ),
        migrations.AddField(
            model_name='nazwagry',
            name='Dostepnosc',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Wybor',
        ),
    ]
