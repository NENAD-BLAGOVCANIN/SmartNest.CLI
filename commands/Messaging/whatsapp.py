import click
from twilio.rest import Client
from config import TWILIO_ACCOUNT_SID, AWILIO_AUTH_TOKEN

@click.command()
@click.argument('contact')
@click.argument('message')
def send_message_on_whatsapp(contact, message):
    """Sends a WhatsApp message to a given contact."""

    click.echo(f"Sending WhatsApp message to {contact}...")

    client = Client(TWILIO_ACCOUNT_SID, AWILIO_AUTH_TOKEN)

    try:
        
        client.messages.create(
            from_='whatsapp:+14155238886',
            body="test",
            to='whatsapp:+38766934835'
        )

        click.echo("Message sent successfully")

    except Exception as e:
        click.echo(f"Failed to send message: {e}")
