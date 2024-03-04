# Generated by Django 5.0.1 on 2024-02-06 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('brand', models.CharField(max_length=256)),
                ('model', models.CharField(max_length=256)),
                ('fuel', models.CharField(choices=[('GASOLINE', 'Gasoline'), ('DIESEL', 'Diesel'), ('ELECTRIC', 'Electric'), ('HYBRID', 'Hybrid'), ('BENZIN', 'Benzin')], max_length=30)),
                ('mileage', models.PositiveBigIntegerField()),
            ],
            options={
                'verbose_name': 'Машина',
                'verbose_name_plural': 'Машины',
            },
        ),
    ]
