# Generated by Django 3.2.2 on 2021-05-24 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shavarma', '0003_positionofpoint_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('com', models.TextField(blank=True)),
                ('tasty', models.FloatField()),
                ('struct', models.FloatField()),
                ('orig', models.FloatField()),
                ('id_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shavarma.positionofpoint')),
            ],
        ),
    ]
