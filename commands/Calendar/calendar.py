from utils.http import send
from utils.auth import get_google_credentials
from datetime import datetime, timedelta
import click

google_calendar_url = "https://www.googleapis.com/calendar/v3/calendars"

today = datetime.utcnow()
time_min = today.isoformat() + 'Z'
time_max = (today + timedelta(days=7)).isoformat() + 'Z'

params = {
    'timeMin': time_min,
    'timeMax': time_max,
    'singleEvents': 'true',
    'orderBy': 'startTime'
}

@click.command()
def get_calendar_events():
    """Fetch calendar events for the next 7 days and summarize them."""
    
    access_token = get_google_credentials()

    events = send('GET', f'{google_calendar_url}/primary/events', 
        headers={"Authorization": f"Bearer {access_token}"},
        params=params
    )

    click.echo(events)



@click.command()
@click.argument('title')
@click.argument('start_datetime')
@click.argument('end_datetime')
def create_calendar_event(title, start_datetime, end_datetime):
    """Create a new calendar event with the given title and datetime parameters."""

    access_token = get_google_credentials()

    event_data = {
        'summary': title,
        'start': {
            'dateTime': datetime.strptime(start_datetime, '%Y-%m-%dT%H:%M:%S').isoformat() + 'Z',
            'timeZone': 'UTC'
        },
        'end': {
            'dateTime': datetime.strptime(end_datetime, '%Y-%m-%dT%H:%M:%S').isoformat() + 'Z',
            'timeZone': 'UTC'
        }
    }

    response = send('POST', f'{google_calendar_url}/primary/events', 
        headers={"Authorization": f"Bearer {access_token}"},
        body=event_data
    )

    click.echo(response)