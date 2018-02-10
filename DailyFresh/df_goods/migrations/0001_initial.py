# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('g_title', models.CharField(max_length=20)),
                ('g_pic', models.ImageField(upload_to='df_goods')),
                ('g_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('g_unit', models.CharField(max_length=20, default='500g')),
                ('g_click', models.IntegerField(default=0)),
                ('g_jianjie', models.CharField(max_length=200)),
                ('g_kucun', models.IntegerField(default=0)),
                ('g_content', tinymce.models.HTMLField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('t_title', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='g_type',
            field=models.ForeignKey(to='df_goods.TypeInfo'),
        ),
    ]
