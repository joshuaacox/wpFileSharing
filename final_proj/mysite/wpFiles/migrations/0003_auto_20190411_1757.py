# Generated by Django 2.2 on 2019-04-11 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wpFiles', '0002_auto_20190411_1716'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='rating',
        ),
        migrations.AlterField(
            model_name='academic_class',
            name='dept_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wpFiles.Academic_dept'),
        ),
        migrations.AlterField(
            model_name='file',
            name='class_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wpFiles.Academic_class'),
        ),
    ]