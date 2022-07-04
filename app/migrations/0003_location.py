# Generated by Django 4.0.5 on 2022-07-04 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_distributor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='firma', max_length=50)),
                ('address', models.CharField(default='firma', max_length=50)),
                ('postalcode', models.CharField(default='firma', max_length=100)),
            ],
        ),
    ]
