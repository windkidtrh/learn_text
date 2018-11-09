# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('the_time', models.DateTimeField()),
                ('info', models.TextField()),
            ],
            options={
                'db_table': 'log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LogDrive',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_type', models.CharField(max_length=8)),
                ('second_type', models.CharField(max_length=8)),
                ('device_nums', models.IntegerField()),
                ('the_time', models.DateTimeField()),
                ('current_status', models.CharField(max_length=20)),
                ('info', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'log_drive',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LogSwitch',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_type', models.CharField(max_length=4)),
                ('second_type', models.CharField(max_length=4)),
                ('product_num', models.CharField(max_length=12)),
                ('the_time', models.DateTimeField()),
                ('info', models.TextField()),
            ],
            options={
                'db_table': 'log_switch',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LogTimer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('timer_id', models.IntegerField()),
                ('first_type', models.CharField(max_length=20)),
                ('second_type', models.CharField(max_length=20)),
                ('product_num', models.CharField(max_length=12)),
                ('state', models.CharField(max_length=20)),
                ('set_time', models.CharField(max_length=20)),
                ('answer_time', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'log_timer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ManageRequest',
            fields=[
                # ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_type', models.CharField(max_length=4)),
                ('second_type', models.CharField(max_length=4)),
                ('product_num', models.CharField(max_length=12)),
                ('life', models.IntegerField()),
                ('request_value', models.IntegerField()),
                ('return_value', models.IntegerField()),
                ('state', models.TextField()),
            ],
            options={
                'db_table': 'manage_request',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_type', models.CharField(max_length=4)),
                ('second_type', models.CharField(max_length=4)),
                ('product_num', models.CharField(max_length=12)),
                ('regist_num', models.CharField(max_length=5)),
                ('mac', models.CharField(max_length=12)),
                ('product_state', models.IntegerField()),
                ('user_id', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductBelongTo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_type', models.CharField(max_length=4)),
                ('second_type', models.CharField(max_length=4)),
                ('product_num', models.CharField(max_length=12)),
                ('user_id', models.IntegerField()),
                ('pro_name', models.CharField(max_length=22)),
            ],
            options={
                'db_table': 'product_belong_to',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCurrentState',
            fields=[
                # ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_type', models.CharField(max_length=4)),
                ('second_type', models.CharField(max_length=4)),
                ('product_num', models.CharField(max_length=12)),
                ('current_state', models.TextField()),
                ('request_state', models.TextField(null=True, blank=True)),
                ('ip_address', models.CharField(max_length=16)),
                ('net_port', models.IntegerField()),
                ('online_value', models.IntegerField()),
            ],
            options={
                'db_table': 'product_current_state',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ProductDescription',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_type', models.CharField(max_length=4)),
                ('second_type', models.CharField(max_length=4)),
                ('property', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'product_description',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RoomProduct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('first_type', models.CharField(max_length=4)),
                ('second_type', models.CharField(max_length=4)),
                ('product_num', models.CharField(max_length=8)),
            ],
            options={
                'db_table': 'room_product',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RoomSetTemp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('room_id', models.IntegerField()),
                ('set_temperature', models.IntegerField()),
            ],
            options={
                'db_table': 'room_set_temp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SaveTmpValue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_value', models.IntegerField()),
            ],
            options={
                'db_table': 'save_tmp_value',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SetTimer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.IntegerField()),
                ('first_type', models.CharField(max_length=20)),
                ('second_type', models.CharField(max_length=20)),
                ('product_num', models.CharField(max_length=12)),
                ('state', models.CharField(max_length=20)),
                ('set_time', models.CharField(max_length=20)),
                ('set_day', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'set_timer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SwitchJoinDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_type', models.CharField(max_length=4)),
                ('second_type', models.CharField(max_length=4)),
                ('product_num', models.CharField(max_length=12)),
                ('target_first_type', models.CharField(max_length=4)),
                ('target_second_type', models.CharField(max_length=4)),
                ('target_product_num', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'switch_join_device',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.CharField(max_length=11)),
                ('user_name', models.CharField(max_length=20)),
                ('user_pwd', models.CharField(max_length=20)),
                ('user_set', models.TextField(null=True, blank=True)),
                ('last_set_time', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
