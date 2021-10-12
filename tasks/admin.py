
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
class Taskadmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','title','created','photo']

admin.site.register(Task,Taskadmin)
