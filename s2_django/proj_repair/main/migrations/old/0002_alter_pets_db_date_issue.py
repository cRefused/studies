# Generated by Django 3.2.25 on 2024-06-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pets_db',
            name='date_issue',
            field=models.DateTimeField(),
        ),
    ]
