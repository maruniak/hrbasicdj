from django.contrib import admin
from django.urls import reverse
from .models import Organization, Employee
from django.utils.html import format_html

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'organization', 'pdf_link')
    readonly_fields = ('photo_thumb',)
    fields = ('name', 'birthday', 'organization', 'photo', 'photo_thumb')    

    def pdf_link(self, obj):
        return format_html(
            '<a href="{}" target="_blank">PDF card</a>',
            reverse('employee_card_pdf', args=[obj.pk])
        )
    pdf_link.short_description = "Card"
    
    def photo_thumb(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height:100px;"/>', obj.photo.url)
        return "-"
    photo_thumb.short_description = "Current Photo"
