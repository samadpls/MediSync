# Generated by Django 4.2.2 on 2023-06-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(max_length=20)),
                ('time_range', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='patient',
            name='id_p',
            field=models.CharField(default='NUZl', max_length=4, primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('specialty', models.CharField(max_length=100)),
                ('availabilities', models.ManyToManyField(to='database.availability')),
            ],
        ),
    ]