# Generated by Django 5.0.2 on 2024-02-26 04:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ijara', '0002_rename_autoturargoh_auto_rename_buyurtma_buyur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auto',
            old_name='model',
            new_name='title',
        ),
    ]
