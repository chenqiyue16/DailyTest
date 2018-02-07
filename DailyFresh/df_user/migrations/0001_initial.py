# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('u_receive_name', models.CharField(max_length=20)),
                ('u_receive_address', models.CharField(max_length=40)),
                ('u_receive_number', models.CharField(max_length=6)),
                ('u_receive_phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('u_name', models.CharField(max_length=20)),
                ('u_pwd', models.CharField(max_length=40)),
                ('u_email', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='useraddress',
            name='u_user',
            field=models.ForeignKey(to='df_user.UserInfo'),
        ),
    ]
