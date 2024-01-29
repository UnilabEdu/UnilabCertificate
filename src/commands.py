import json
import requests
import click

from flask.cli import with_appcontext

from src.extensions import db

from src.models import User


@click.command("api_test")
@with_appcontext
def api_test():
    # # api/login
    # link = "http://127.0.0.1:5000/users_id"
    # headers = {"Content-Type": "application/json"}
    # body = {"username": 'TestUser',"password":"TestUser"}

    # api/certificate
    # link = "http://127.0.0.1:5000/api/certificate"
    # headers = {"Content-Type": "application/json",
    #            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNTUxOTMyMSwianRpIjoiMjk1NjNjNWYtZjQ0Yi00Nzg0LWIxMWUtYjk4NzUwYzdkOGFiIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzA1NTE5MzIxLCJjc3JmIjoiNzE1OGJiNTQtZWUzZC00NWVlLTlkOTctMTkxMjMzY2Y3ZDY1IiwiZXhwIjoxNzA1NTIwMjIxfQ.4VU4xqXAltG8P98xVVykQI4JPeL2wn_H-2qm53Yi_ME"}
    # body = {"username": 'TestUser', "date": '2004-12-01', "type": "TestType"}


    link = "http://127.0.0.1:5000/api/get_certificate"
    headers = {"Content-Type": "application/json"}
    body = {"uuid": "0de8c984-c766-4ac3-ab0d-bc48fe711ce6"}

    received_response = requests.get(link, data=json.dumps(body), headers=headers)
    print(received_response.content)


@click.command("init_db")
@with_appcontext
def init_db():
    click.echo("Database creation in progress")
    db.drop_all()
    db.create_all()
    test_user = User(username="TestUser", password="TestUser")
    test_user.create()
    click.echo("Done!")
