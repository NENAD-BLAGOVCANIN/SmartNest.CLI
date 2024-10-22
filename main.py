import click
import importlib
import pkgutil
import commands
from commands.play_song import play_song
from commands.weather import get_local_weather
from commands.Calendar.calendar import get_calendar_events, create_calendar_event
from commands.Tasks.tasks import get_tasks, create_task

@click.group()
def cli():
    """Smartnest CLI Tool"""
    pass

def load_commands():
    cli.add_command(play_song)
    cli.add_command(get_local_weather)
    cli.add_command(get_calendar_events)
    cli.add_command(create_calendar_event)
    cli.add_command(get_tasks)
    cli.add_command(create_task)

load_commands()

if __name__ == '__main__':
    cli()
