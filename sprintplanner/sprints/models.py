from django.db import models

# Create your models here.
class Sprint(models.Model):
	summary = models.CharField(max_length=200)
	location = models.CharField(max_length=200)
	#dates for start and end for sprints, might need to use DateField so that only all day events are entered to the calendar
	start = models.DateTimeField('start date')
	end = models.DateTimeField('end date')
	#organiser and attendee information
	organizer = models.CharField(max_length=200)

	def __str__(self):
		return self.summary

class Attendee(models.Model):
	assigned_sprint = models.ForeignKey(Sprint)
	email = models.CharField(max_length=200)
	displayName = models.CharField(max_length=200)
	role = models.CharField(max_length=200)
	
	def __str__(self):
		return self.email


		




