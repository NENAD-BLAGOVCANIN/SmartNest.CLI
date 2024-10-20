import click
import requests
from config import OPENWEATHERMAP_API_KEY, CITY

@click.command()
def get_local_weather():

    url = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={OPENWEATHERMAP_API_KEY}&units=metric'
    
    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            city_name = data['name']
            temperature = data['main']['temp']
            weather_description = data['weather'][0]['description']

            click.echo(f"Weather in {city_name}:")
            click.echo(f"Temperature: {temperature}°C")
            click.echo(f"Condition: {weather_description.capitalize()}")
        else:
            click.echo(f"Error: {data['message']}")
    except Exception as e:
        click.echo(f"Failed to retrieve weather data: {e}")
