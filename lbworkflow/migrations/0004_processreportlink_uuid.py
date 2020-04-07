# Generated by Django 3.0.4 on 2020-04-07 02:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('lbworkflow', '0003_auto_20200221_0438'),
    ]

    operations = [
        migrations.AddField(
            model_name='processreportlink',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
