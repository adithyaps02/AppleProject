# Generated by Django 4.2.5 on 2023-10-03 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookName', models.CharField(blank=True, max_length=100, null=True)),
                ('Definition', models.CharField(blank=True, max_length=100, null=True)),
                ('BookImage', models.ImageField(blank=True, null=True, upload_to='BookImage')),
            ],
        ),
        migrations.DeleteModel(
            name='CategoryDb',
        ),
    ]
