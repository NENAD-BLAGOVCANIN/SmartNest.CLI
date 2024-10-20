from utils.http import send
from datetime import datetime, timedelta
import click
from utils.auth import get_google_credentials

tasklist_id = "NjlnYURpWXBPN0M0ajVtQg"
google_tasks_url = f"https://www.googleapis.com/tasks/v1/lists/{tasklist_id}/tasks"

@click.command()
def get_tasks():
    """Fetch tasks from Google Tasks."""

    access_token = get_google_credentials()

    tasks = send('GET', f'{google_tasks_url}', 
        headers={"Authorization": "Bearer " + access_token},
    )

    click.echo(tasks)
