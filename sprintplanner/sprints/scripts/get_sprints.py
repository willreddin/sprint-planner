from sprints.models import Sprint, Attendee

def run():
	#Get all Sprint summaries
	Sprint_summaries = Sprint.objects.all(summaries)
	print(Sprint_summaries)