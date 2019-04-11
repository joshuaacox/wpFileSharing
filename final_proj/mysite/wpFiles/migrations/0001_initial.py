# Generated by Django 2.1.5 on 2019-04-09 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='academic_class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_code', models.CharField(max_length=5, unique=True)),
                ('class_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='academic_dept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_code', models.CharField(max_length=10, unique=True)),
                ('dept_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_alias', models.CharField(max_length=30, unique=True)),
                ('document', models.FileField(upload_to='documents/')),
                ('rating', models.IntegerField(null=True)),
                ('downloads', models.IntegerField(default=0)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('class_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wpFiles.academic_class')),
            ],
        ),
        migrations.AddField(
            model_name='academic_class',
            name='dept_code',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wpFiles.academic_dept'),
        ),
    ]
