# Generated by Django 4.2.6 on 2023-10-28 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('breaks', '0008_replacementemployee'),
    ]

    operations = [
        migrations.CreateModel(
            name='BreakStatus',
            fields=[
                ('code', models.CharField(max_length=16, primary_key=True, serialize=False, verbose_name='Код')),
                ('name', models.CharField(max_length=32, verbose_name='Название')),
                ('sort', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Сотрировка')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
            ],
            options={
                'verbose_name': 'Статус обеда',
                'verbose_name_plural': 'Статусы обеды',
            },
        ),
        migrations.AlterModelOptions(
            name='replacementstatus',
            options={'verbose_name': 'Статус смены', 'verbose_name_plural': 'статусы смены'},
        ),
    ]
