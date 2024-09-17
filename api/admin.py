from django.contrib import admin
from .models import Company, Employee
# Register your models here.
# to list the required details write it in this way...
class CompanyAdmin(admin.ModelAdmin):
    list_display= ('name', 'location', 'type')
    search_fields=('name', 'location', 'type')
    list_filter=('name', 'location', 'type')
admin.site.register(Company, CompanyAdmin)
# admin.site.register(Company)
class EmployeeAdmin(admin.ModelAdmin):
    list_display= ('name', 'address', 'position', 'company')
    search_fields= ('name', 'address', 'position')
    list_filter= ('name', 'address', 'position', 'company',)
    

admin.site.register(Employee, EmployeeAdmin)

