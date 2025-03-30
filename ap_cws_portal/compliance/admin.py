from django.contrib import admin
from .models import GIGWRequirement

@admin.register(GIGWRequirement)
class GIGWRequirementAdmin(admin.ModelAdmin):
    list_display = ('section', 'requirement_short', 'is_implemented', 'last_verified')
    list_filter = ('is_implemented', 'section')
    search_fields = ('requirement', 'implementation')
    ordering = ('section',)
    
    def requirement_short(self, obj):
        return obj.requirement[:50] + '...' if len(obj.requirement) > 50 else obj.requirement
    requirement_short.short_description = 'Requirement'