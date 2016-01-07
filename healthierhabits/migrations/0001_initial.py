# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100, blank=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('email1', models.CharField(max_length=100)),
                ('email2', models.CharField(max_length=100, blank=True)),
                ('phone1', models.CharField(max_length=100, blank=True)),
                ('phone2', models.CharField(max_length=100, blank=True)),
                ('current_points', models.BigIntegerField(default=0)),
                ('life_points', models.BigIntegerField(default=0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('address1', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100, blank=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name='purchase date', default=django.utils.timezone.now)),
                ('item', models.CharField(max_length=200)),
                ('price', models.IntegerField(default=1)),
                ('filled', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(to='healthierhabits.Customers')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='customers',
            name='group',
            field=models.ForeignKey(to='healthierhabits.Groups'),
            preserve_default=True,
        ),
    ]
