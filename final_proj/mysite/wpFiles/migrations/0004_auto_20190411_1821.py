# Generated by Django 2.2 on 2019-04-11 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wpFiles', '0003_auto_20190411_1757'),
    ]

    operations = [
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
