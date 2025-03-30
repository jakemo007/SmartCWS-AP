from django.contrib import admin
from .models import ZonalApproval

@admin.register(ZonalApproval)
class ZonalApprovalAdmin(admin.ModelAdmin):
    list_display = ('ulb_verification', 'status', 'approved_by', 'inspection_date')
    list_filter = ('status',)
    search_fields = ('ulb_verification__space__name', 'apiic_reference')
    raw_id_fields = ('ulb_verification', 'approved_by')