# Generated by Django 4.1 on 2022-08-19 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_coach_followers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('image', models.ImageField(default='service.jpg', upload_to='service_pictures')),
                ('description', models.TextField()),
            ],
        ),
    ]
