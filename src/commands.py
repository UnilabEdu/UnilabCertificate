import json

import requests
from flask.cli import with_appcontext
import click

from src.extensions import db


@click.command("init_db")
@with_appcontext
def init_db():

    link = "http://127.0.0.1:5000/users_id"
    headers = {"Content-Type": "application/json"}
    body = {"name": "oto", "password": "oto"}

    received_responce = requests.post(link,data=json.dumps(body),headers=headers)
    print(received_responce.content)


    click.echo("Database creation in progress")
    # db.drop_all()
    # db.create_all()
    click.echo("Done!")