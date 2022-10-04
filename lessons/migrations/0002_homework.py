# Generated by Django 4.0.6 on 2022-09-01 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='image/')),
                ('file', models.FileField(upload_to='files/')),
            ],
        ),
    ]