# Generated by Django 3.0.4 on 2020-03-21 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='descriptions',
            new_name='description',
        ),
    ]
