import click
import requests
import os
import json
from config import GITHUB_ACCESS_TOKEN

TOKEN_FILE = 'token.json'

def load_github_token():
    """Load the GitHub token from token.json if it exists."""
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as token_file:
            tokens = json.load(token_file)
            return tokens.get('github', {}).get('token')
    return None

@click.command()
@click.argument('project_name')
def create_new_github_project(project_name):
    """Create a new GitHub repository with the given project name."""

    url = 'https://api.github.com/user/repos'

    headers = {
        'Authorization': f'token {GITHUB_ACCESS_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }

    payload = {
        'name': project_name,
        'description': f'Repository for {project_name}',
        'private': False
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 201:
        click.echo(f"Successfully created repository: {project_name}")
        repo_url = response.json().get('html_url')
        click.echo(f"Repository URL: {repo_url}")
    else:
        click.echo(f"Failed to create repository: {response.json().get('message')}")