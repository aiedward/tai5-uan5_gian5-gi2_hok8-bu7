# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-21 12:41
from __future__ import unicode_literals

from django.db import migrations, models
import 臺灣言語服務.models檢查


class Migration(migrations.Migration):

    dependencies = [
        ('臺灣言語服務', '0006_auto_20171221_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='訓練過渡格式',
            name='外文',
            field=models.TextField(blank=True, null=True, validators=[臺灣言語服務.models檢查.檢查敢是分詞]),
        ),
        migrations.AlterField(
            model_name='訓練過渡格式',
            name='文本',
            field=models.TextField(blank=True, null=True, validators=[臺灣言語服務.models檢查.檢查敢是分詞]),
        ),
    ]
