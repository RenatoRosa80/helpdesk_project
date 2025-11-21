from django.contrib import admin
from .models import Ticket, TicketHistory

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'status', 'assigned_to', 'assigned_team', 'created_at')
    list_filter = ('status', 'category', 'assigned_team', 'priority')
    search_fields = ('title', 'description', 'created_by__username', 'assigned_to__username')
    readonly_fields = ('created_at',)

@admin.register(TicketHistory)
class TicketHistoryAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'timestamp', 'actor', 'action')
    list_filter = ('actor',)
    search_fields = ('action', 'note')
