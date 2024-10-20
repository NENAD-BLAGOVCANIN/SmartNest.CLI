import click
from googleapiclient.discovery import build
from config import GOOGLE_API_KEY
import webbrowser

@click.command()
@click.argument('song_name')
def play_song(song_name):

    click.echo(f"Playing the song: {song_name}")
    
    youtube = build('youtube', 'v3', developerKey=GOOGLE_API_KEY)
    
    request = youtube.search().list(
        part='snippet',
        q=song_name,
        type='video',
        maxResults=1
    )
    response = request.execute()
    
    video_id = response['items'][0]['id']['videoId']
    
    video_url = f"https://www.youtube.com/watch?v={video_id}"
    webbrowser.open(video_url)

    return video_url