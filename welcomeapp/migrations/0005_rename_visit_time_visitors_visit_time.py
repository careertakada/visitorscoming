# Generated by Django 3.2 on 2022-07-13 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('welcomeapp', '0004_visitors_visit_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitors',
            old_name='Visit_time',
            new_name='visit_time',
        ),
    ]
