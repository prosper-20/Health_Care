# Generated by Django 4.1 on 2022-08-15 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_email_subscription_subscriber_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='BMI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weight', models.FloatField(help_text='Kg')),
                ('height', models.FloatField(help_text='Cm')),
            ],
        ),
    ]