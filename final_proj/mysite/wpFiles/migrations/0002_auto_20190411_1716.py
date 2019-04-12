# Generated by Django 2.1.5 on 2019-04-11 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wpFiles', '0001_initial'),
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
