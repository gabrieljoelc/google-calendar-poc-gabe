# Gabe's crappy google calendar API thingy

## Getting started

Prerequisites:
- Follow steps in Google API credentials section to get a `credentials.json`

Steps:
1. Install dependencies (TODO: use the requirements.txt thingy)
```
pip install Flask
pip install google
pip install google-auth
pip install google-auth-oauthlib
pip install google-api-python-client
```
2. Run the app:
```
python fetch_events.py
```
3. Open http://localhost:4000
4. Authenticate with the Google Calendar you want and allow access

You should see the events listed in the browser for the dates specified in the script.

## Google API credentials

1. Create a Google Cloud Project
- Go to the Google Cloud Console: https://console.cloud.google.com/
- Click on the project drop-down and create a new project or select an existing project.
- Make sure you are using a billing-enabled project as some Google APIs may require billing information.
2. Enable the Google Calendar API:
- In your Google Cloud Project, navigate to the "APIs & Services" > "Library" page.
- Search for "Google Calendar API" and click on it.
- Click the "Enable" button to enable the Google Calendar API for your project.
3. Create OAuth 2.0 Credentials:
- In the Google Cloud Console, go to "APIs & Services" > "Credentials."
- Click on the "Create Credentials" dropdown and select "OAuth client ID."
- Configure the OAuth consent screen by specifying details like the application name and user support email.
- Select the application type that best fits your use case (e.g., "Desktop app" or "Web application").
- Set up the authorized redirect URIs. This is where users will be redirected after granting permissions.
- Click the "Create" button to create the OAuth 2.0 client ID.
4. Download credentials.json:
- After creating the OAuth client ID, you should see a page with your client ID and client secret.
- Click on the "Download" button next to the client ID to download the credentials.json file. This file contains the client ID and client secret needed for authentication.
5. Use credentials.json in Your Application:
- Place the downloaded credentials.json file in your application's directory.
- When you run your application, it will use this JSON file to authenticate with Google services.
