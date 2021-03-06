"""A quickstart example showing usage of the Google Calendar API."""
from datetime import datetime
import os

from apiclient.discovery import build
from httplib2 import Http
import oauth2client
from oauth2client import client
from oauth2client import tools

from sprints.models import Sprint, Attendee 

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
CLIENT_SECRET_FILE = 'client_secret.json'
APPLICATION_NAME = 'Calendar API Quickstart'


def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'calendar-api-quickstart.json')

    store = oauth2client.file.Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatability with Python 2.6
            credentials = tools.run(flow, store)
        print ('Storing credentials to ' + credential_path)
    return credentials

q = Sprint.objects.get(pk=1)

event = {
	'summary': q.summary, 
	'location': q.location, 
	'start': {
		'datetime': q.start
	}, 
	'end': {
		'datetime': q.end
	},
	'attendees': [
		{
		'email': q.attendee_set.get(pk=1)
		}
	],
}

created_event = service.events().insert(calendarId='willreddin88@gmail.com', body=event).execute()

print (created_event['id'])