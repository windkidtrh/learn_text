from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test1(models.Model):
	name = models.CharField(max_length=20)
	age  = models.IntegerField()
	sex  = models.IntegerField()
	class Meta:
		managed = False
		db_table = 'test1'
	
	def _str_(self):
		return self.name.encode('utf-8')