# single_desk/admin.py
from django.contrib import admin
from .models import BusinessRegistration

@admin.register(BusinessRegistration)
class BusinessRegistrationAdmin(admin.ModelAdmin):
    list_display = ('business_name', 'registration_number', 'status')
    search_fields = ('business_name', 'registration_number')
    list_filter = ('status', 'business_type')