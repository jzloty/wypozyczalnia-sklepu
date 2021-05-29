# Generated by Django 3.2.2 on 2021-05-26 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gry', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choice',
            new_name='Wybor',
        ),
        migrations.AlterModelOptions(
            name='nazwagry',
            options={'verbose_name_plural': 'Nazwy Gier'},
        ),
        migrations.RenameField(
            model_name='nazwagry',
            old_name='Tytyl',
            new_name='Tytul',
        ),
        migrations.AlterField(
            model_name='nazwagry',
            name='add_date',
            field=models.DateTimeField(null=True, verbose_name='data dodania'),
        ),
    ]
