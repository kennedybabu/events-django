# Generated by Django 4.0 on 2023-10-31 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_event', '0002_event_due'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='ticket_price',
            field=models.CharField(max_length=8, null=True),
        ),
    ]
