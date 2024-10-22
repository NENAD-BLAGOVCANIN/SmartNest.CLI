import click
from commands.youtube import play_youtube_video
from commands.weather import get_local_weather
from commands.Calendar.calendar import get_calendar_events, create_calendar_event
from commands.Tasks.tasks import get_tasks, create_task
from commands.Messaging.whatsapp import send_message_on_whatsapp

@click.group()
def cli():
    """Smartnest CLI Tool"""
    pass

def load_commands():
    cli.add_command(play_youtube_video)
    cli.add_command(get_local_weather)
    cli.add_command(get_calendar_events)
    cli.add_command(create_calendar_event)
    cli.add_command(get_tasks)
    cli.add_command(create_task)
    cli.add_command(send_message_on_whatsapp)

load_commands()

if __name__ == '__main__':
    cli()
