# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthierhabits', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rewards',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=100)),
                ('available', models.BooleanField(default=True)),
                ('number_given', models.IntegerField(default=100)),
                ('group', models.ForeignKey(to='healthierhabits.Groups')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
