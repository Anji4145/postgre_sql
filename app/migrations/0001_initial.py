# Generated by Django 4.2.3 on 2023-10-03 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scname', models.CharField(max_length=20)),
                ('sname', models.CharField(max_length=20)),
            ],
        ),
    ]
