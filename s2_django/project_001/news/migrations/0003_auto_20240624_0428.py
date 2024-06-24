# Generated by Django 3.2.25 on 2024-06-24 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20240624_0418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news_db',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='news.category_db', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='news_db',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]
