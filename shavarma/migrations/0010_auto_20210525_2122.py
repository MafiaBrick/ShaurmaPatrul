# Generated by Django 3.2.2 on 2021-05-25 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shavarma', '0009_auto_20210524_2009'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Коментарий', 'verbose_name_plural': 'Коментарии'},
        ),
        migrations.AlterModelOptions(
            name='positionofpoint',
            options={'verbose_name': 'Позиция', 'verbose_name_plural': 'Позиции'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='com',
            field=models.TextField(blank=True),
        ),
    ]