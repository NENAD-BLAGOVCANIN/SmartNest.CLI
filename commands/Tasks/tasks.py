from utils.http import send
import click
from utils.auth import get_google_credentials

tasklist_id = "NjlnYURpWXBPN0M0ajVtQg"
google_tasks_url = f"https://www.googleapis.com/tasks/v1/lists/{tasklist_id}/tasks"

@click.command()
def get_tasks():
    """Fetch tasks from Google Tasks."""

    access_token = get_google_credentials()

    tasks = send('GET', google_tasks_url, 
        headers={"Authorization": "Bearer " + access_token},
    )

    click.echo(tasks)


@click.command()
@click.argument('title')
def create_task(title):
    """Create a new task in Google Tasks with the given title."""

    access_token = get_google_credentials()

    task_data = {
        'title': title
    }

    response = send('POST', google_tasks_url, 
        headers={"Authorization": "Bearer " + access_token},
        body=task_data
    )

    click.echo(response)