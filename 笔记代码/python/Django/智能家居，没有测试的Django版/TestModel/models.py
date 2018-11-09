# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
import json

class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Log(models.Model):
    # id = models.AutoField(unique=True)
    user_id = models.IntegerField()
    the_time = models.DateTimeField()
    info = models.TextField()

    class Meta:
        managed = False
        db_table = 'log'
        unique_together = (('id', 'user_id'),)


class LogDrive(models.Model):
    first_type = models.CharField(max_length=8)
    second_type = models.CharField(max_length=8)
    device_nums = models.IntegerField()
    the_time = models.DateTimeField()
    current_status = models.CharField(max_length=20)
    info = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'log_drive'


class LogSwitch(models.Model):
    first_type = models.CharField(max_length=4)
    second_type = models.CharField(max_length=4)
    product_num = models.CharField(max_length=12)
    the_time = models.DateTimeField()
    info = models.TextField()

    class Meta:
        managed = False
        db_table = 'log_switch'


class LogTimer(models.Model):
    user_id = models.IntegerField()
    timer_id = models.IntegerField()
    first_type = models.CharField(max_length=20)
    second_type = models.CharField(max_length=20)
    product_num = models.CharField(max_length=12)
    state = models.CharField(max_length=20)
    set_time = models.CharField(max_length=20)
    answer_time = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'log_timer'


class ManageRequest(models.Model):
    first_type = models.CharField(max_length=4)
    second_type = models.CharField(max_length=4)
    product_num = models.CharField(max_length=12)
    life = models.IntegerField()
    request_value = models.IntegerField(primary_key=True)
    return_value = models.IntegerField()
    state = models.TextField()

    class Meta:
        managed = False
        db_table = 'manage_request'
        unique_together = (('first_type', 'second_type', 'product_num'),)
    
    def __unicode__(self):
        return_mysql = (self.first_type,self.second_type,self.product_num,self.life,self.request_value,self.return_value,self.state)
        return json.dumps(return_mysql)

class Product(models.Model):
    first_type = models.CharField(max_length=4,primary_key=True)
    second_type = models.CharField(max_length=4)
    product_num = models.CharField(max_length=12)
    regist_num = models.CharField(max_length=5)
    mac = models.CharField(max_length=12)
    product_state = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
        unique_together = (('first_type', 'second_type', 'product_num'),)


class ProductBelongTo(models.Model):
    # id = models.AutoField(unique=True)
    first_type = models.CharField(max_length=4)
    second_type = models.CharField(max_length=4)
    product_num = models.CharField(max_length=12)
    user_id = models.IntegerField()
    pro_name = models.CharField(max_length=22)

    class Meta:
        managed = False
        db_table = 'product_belong_to'
        unique_together = (('product_num', 'first_type', 'second_type', 'user_id'),)


    def __unicode__(self):
        return_mysql = (self.id,self.first_type,self.second_type,self.product_num,self.user_id,self.pro_name)
        return json.dumps(return_mysql)

class ProductCurrentState(models.Model):
    first_type = models.CharField(max_length=4)
    second_type = models.CharField(max_length=4)
    product_num = models.CharField(max_length=12)
    current_state = models.TextField()
    request_state = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=16)
    net_port = models.IntegerField()
    online_value = models.IntegerField()
    belong_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'product_current_state'
        unique_together = (('first_type', 'second_type', 'product_num'),)

    def __unicode__(self):
        return_mysql = (self.first_type,self.second_type,self.product_num,self.current_state,self.request_state,self.ip_address,self.net_port,self.online_value,self.belong_id)
        return json.dumps(return_mysql)

class ProductDescription(models.Model):
    first_type = models.CharField(max_length=4)
    second_type = models.CharField(max_length=4)
    property = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_description'
        unique_together = (('first_type', 'second_type'),)


class RoomProduct(models.Model):
    rp_id = models.IntegerField(primary_key=True)
    room_id = models.IntegerField()
    product_id = models.IntegerField()
    first_type = models.CharField(max_length=4)
    second_type = models.CharField(max_length=4)
    product_num = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'room_product'


class RoomSetTemp(models.Model):
    room_id = models.IntegerField()
    set_temperature = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'room_set_temp'


class SaveTmpValue(models.Model):
    id = models.IntegerField(primary_key=True)
    last_value = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'save_tmp_value'

    def __unicode__(self):
        return_mysql = (self.id,self.last_value)
        return json.dumps(return_mysql)

class SetTimer(models.Model):
    timer_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField()
    first_type = models.CharField(max_length=20)
    second_type = models.CharField(max_length=20)
    product_num = models.CharField(max_length=12)
    state = models.CharField(max_length=20)
    set_time = models.CharField(max_length=20)
    set_day = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'set_timer'


class SwitchJoinDevice(models.Model):
    first_type = models.CharField(max_length=4,primary_key=True)
    second_type = models.CharField(max_length=4)
    product_num = models.CharField(max_length=12)
    target_first_type = models.CharField(max_length=4)
    target_second_type = models.CharField(max_length=4)
    target_product_num = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'switch_join_device'
        unique_together = (('first_type', 'second_type', 'product_num', 'target_first_type', 'target_second_type', 'target_product_num'),)

    def __unicode__(self):
        return_mysql = (self.first_type,self.second_type,self.product_num,self.target_first_type,self.target_second_type,self.target_product_num)
        return json.dumps(return_mysql)

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    phone = models.CharField(max_length=11)
    user_name = models.CharField(max_length=20)
    user_pwd = models.CharField(max_length=20)
    user_set = models.TextField(blank=True, null=True)
    last_set_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
