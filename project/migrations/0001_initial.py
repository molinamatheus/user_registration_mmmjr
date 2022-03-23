# Generated by Django 4.0.3 on 2022-03-22 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, default='', max_length=100)),
                ('email', models.CharField(blank=True, default='', max_length=256)),
                ('password', models.CharField(blank=True, default='', max_length=100)),
                ('birthday', models.DateTimeField()),
            ],
        ),
    ]
