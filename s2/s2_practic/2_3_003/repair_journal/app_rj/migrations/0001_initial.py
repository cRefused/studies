# Generated by Django 3.2.25 on 2024-06-27 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='equipment_name_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=32, verbose_name='Наименование')),
            ],
            options={
                'verbose_name': 'Наименование',
                'verbose_name_plural': 'Наименование',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='otdel_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=32, verbose_name='Отделы')),
            ],
            options={
                'verbose_name': 'Отдел',
                'verbose_name_plural': 'Отделы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='tech_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inv_num', models.CharField(max_length=32, verbose_name='Инв. номер')),
                ('defect', models.TextField(verbose_name='Неисправность')),
                ('work_done', models.TextField(blank=True, verbose_name='Проделаная работа')),
                ('date_accept', models.DateField(verbose_name='Дата приемки')),
                ('date_issue', models.DateField(blank=True, null=True, verbose_name='Дата выдачи')),
                ('equipment_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app_rj.equipment_name_db', verbose_name='Наименование')),
                ('otdel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='app_rj.otdel_db', verbose_name='Отдел')),
            ],
            options={
                'verbose_name': 'Тенику',
                'verbose_name_plural': 'Теника',
                'ordering': ['-id', '-date_accept'],
            },
        ),
    ]
