# Generated by Django 4.0.5 on 2023-01-02 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('debtors', '0007_imported_registry_registry_headers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='debtors.departments', verbose_name='Подразделение'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='debtors.positions', verbose_name='Должность'),
        ),
    ]
