from django.contrib import admin

# Register your models here.
from .models import Sprint, Attendee

class AttendeeInLine(admin.TabularInline):
	model = Attendee
	extra = 2

class SprintAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['summary', 'location', 'organizer']}),
		('Date information', {'fields': ['start', 'end']}),
	]
	inlines = [AttendeeInLine]
	list_display = ('summary', 'start', 'end', 'organizer')
		

admin.site.register(Sprint, SprintAdmin)