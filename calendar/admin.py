from django.contrib import admin
from .models import CalendarEvent

@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'category', 'is_approved', 'is_modified')
    list_filter = ('is_approved', 'category', 'date')
    list_editable = ('is_approved', 'is_modified')
    search_fields = ('title', 'description')
    actions = ['approve_events']

    @admin.action(description="Approve selected events")
    def approve_events(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, "Selected events have been approved.")