# Generated by Django 3.2.25 on 2024-06-21 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20240621_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tech_db',
            name='work_done',
            field=models.TextField(blank=True, verbose_name='Проделаная работа'),
        ),
    ]
