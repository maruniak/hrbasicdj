from django.contrib import admin
from .models import Organization, Employee

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'organization')
    list_filter = ('organization',)
    search_fields = ('name',)
