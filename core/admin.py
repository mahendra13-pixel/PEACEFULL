from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # Show the person's name FIRST in the list
    list_display = ('name', 'email', 'phone', 'room_type', 'created_at')

    # Clicking anywhere on the row opens the record
    list_display_links = ('name', 'email')

    # Search by name / email / phone
    search_fields = ('name', 'email', 'phone')

    # Filter sidebar
    list_filter = ('room_type', 'created_at')

    # Read-only audit fields
    readonly_fields = ('created_at',)

    # Order: newest first
    ordering = ('-created_at',)

    # Pagination
    list_per_page = 25

    # Nicer column headers
    @admin.display(description='Room Type', ordering='room_type')
    def room_type(self, obj):
        return obj.get_room_type_display()

    # Page title shows the person's name when viewing/editing
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        if object_id:
            obj = self.get_object(request, object_id)
            if obj:
                extra_context['title'] = f"Contact: {obj.name}"
        return super().changeform_view(request, object_id, form_url, extra_context)