# Generated by Django 3.2.2 on 2021-05-20 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shavarma', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shavarmamodel',
            options={'verbose_name': 'Точка', 'verbose_name_plural': 'Точки'},
        ),
        migrations.AlterField(
            model_name='shavarmamodel',
            name='image',
            field=models.ImageField(upload_to='shavarma/images'),
        ),
        migrations.CreateModel(
            name='positionOfPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('id_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shavarma.shavarmamodel')),
            ],
        ),
    ]