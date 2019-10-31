# Generated by Django 2.2.6 on 2019-10-31 09:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.CharField(max_length=10)),
                ('des', models.CharField(max_length=10)),
                ('doj', models.DateTimeField(default=django.utils.timezone.now)),
                ('hashTravel', models.CharField(max_length=100)),
                ('sampleData', models.CharField(max_length=100)),
            ],
        ),
    ]