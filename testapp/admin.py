from django.contrib import admin
from testapp.models import Employee
# Register your models here.

class EmpData(admin.ModelAdmin):
    list_display=['eno','ename']

admin.site.register(Employee,EmpData)
