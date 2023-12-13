import json
import requests
import click

from flask.cli import with_appcontext

from src.extensions import db


@click.command("api_test")
@with_appcontext
def api_test():
    link = "http://127.0.0.1:5000/api/register"
    headers = {"Content-Type": "application/json"}
    body = {"name": "oto", "password": "oto"}
    received_response = requests.post(link, data=json.dumps(body), headers=headers)
    print(received_response.content)


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Database creation in progress")
    db.drop_all()
    db.create_all()
    click.echo("Done!")