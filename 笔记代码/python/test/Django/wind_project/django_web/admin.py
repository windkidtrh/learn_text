#coding:utf-8
from django.contrib import admin
from models import *

# Register your models here.
class Test1Admin(admin.ModelAdmin):
	list_display = ['id','name','age','sex']#显示完整内容
	search_fields = ('name',)#使用搜索
	fieldsets = (#分块
		['Main',
			{
				'fields':('name',),
			}
		],
		['Advance',
			{

				'fields':('age','sex'),
			}
		],
	)

admin.site.register(Test1,Test1Admin)
