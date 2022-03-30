# Generated by Django 4.0.3 on 2022-03-30 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='newBooking',
            fields=[
                ('cname', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('form', models.FileField(blank=True, upload_to='files')),
                ('pan', models.FileField(blank=True, upload_to='files')),
                ('aadhar', models.FileField(blank=True, upload_to='files')),
                ('booking_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
    ]
