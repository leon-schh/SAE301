# Generated by Django 4.2.1 on 2023-11-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('prise', '0002_delete_livre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etat_checkbox', models.BooleanField(default=False)),
            ],
        ),
    ]
