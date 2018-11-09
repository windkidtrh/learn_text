from django.contrib import admin
from TestModel.models import Test,Register,Contact,Tag
 
# Register your models here.
# admin.site.register([Test,Register,Contact,Tag])
class ContactAdmin(admin.ModelAdmin):
    fieldsets = (
        ['Main',{
            'fields':('name',),
        }],
        ['Advance',{
            'classes': ('collapse',), # CSS
            'fields': ('passwd',),
        }]
    )
 
admin.site.register(Register, ContactAdmin)
admin.site.register([Test, Tag])