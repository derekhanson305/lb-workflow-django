# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-10-19 05:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lbworkflow', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='transition',
        ),
        migrations.AddField(
            model_name='event',
            name='act_name',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='node',
            name='node_type',
            field=models.CharField(choices=[('node', 'Node'), ('router', 'Router')], default='node', max_length=16, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='event',
            name='act_type',
            field=models.CharField(choices=[('transition', 'Transition'), ('agree', 'Agree'), ('edit', 'Edit'), ('give up', 'Give up'), ('reject', 'Reject'), ('back to', 'Back to'), ('rollback', 'Rollback'), ('comment', 'Comment'), ('assign', 'Assign'), ('hold', 'Hold'), ('unhold', 'Unhold')], default='transition', max_length=255),
        ),
        migrations.AlterField(
            model_name='node',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('given up', 'Given up'), ('rejected', 'Rejected'), ('in progress', 'In Progress'), ('completed', 'Completed')], default='in progress', max_length=16, verbose_name='Status'),
        ),
    ]
