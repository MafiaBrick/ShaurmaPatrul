# Generated by Django 3.2.2 on 2021-05-31 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shavarma', '0013_comment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='positionofpoint',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='positionofpoint',
            name='weight',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
