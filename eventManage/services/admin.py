from django.contrib import admin
from services.models import Event, Ticket,volunteer

class EventAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'date', 'description']
# Register your models here.
admin.site.register(Event, EventAdmin)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id','name','event', 'email', 'phone', 'created_at']
admin.site.register(Ticket, TicketAdmin)
class volunteeradmin(admin.ModelAdmin):
    list_display = ['id','name','event']
admin.site.register(volunteer, volunteeradmin)