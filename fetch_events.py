from flask import Flask, request, redirect
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Define your OAuth 2.0 credentials JSON file path
credentials_file = 'credentials.json'

# Define the redirect URI (must match the one in your Google Cloud Console)
redirect_uri = 'http://localhost:4000/oauth2callback'

# Define the scopes you need
scopes = ['https://www.googleapis.com/auth/calendar.readonly']

# Initialize Flask app
app = Flask(__name__)

def create_and_run_flask_app():
    @app.route('/')
    def index():
        # Redirect to Google OAuth2 consent page
        flow = InstalledAppFlow.from_client_secrets_file(
            credentials_file, scopes=scopes, redirect_uri=redirect_uri)
        auth_url, _ = flow.authorization_url()
        return redirect(auth_url)

    @app.route('/oauth2callback')
    def oauth2callback():
        # Handle OAuth2 callback and retrieve credentials
        flow = InstalledAppFlow.from_client_secrets_file(
            credentials_file, scopes=scopes, redirect_uri=redirect_uri)
        flow.fetch_token(code=request.args.get('code'))
        credentials = flow.credentials

        # Initialize the Google Calendar API service
        service = build('calendar', 'v3', credentials=credentials)

        # Fetch upcoming events
        events_result = service.events().list(
            calendarId='primary',
            timeMin='2023-01-01T00:00:00Z',
            maxResults=10,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        events = events_result.get('items', [])

        # Display the events
        if not events:
            return 'No upcoming events found.'
        else:
            event_list = []
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                event_list.append(f'{start} - {event["summary"]}')

            # Display the events in a simple HTML list
            return '<ul>' + ''.join([f'<li>{event}</li>' for event in event_list]) + '</ul>'

    # Start the Flask web server
    app.run(port=4000)

if __name__ == '__main__':
    create_and_run_flask_app()

