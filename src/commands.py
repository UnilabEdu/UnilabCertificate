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
    link = "http://127.0.0.1:5000/api/login"
    headers = {"Content-Type": "application/json"}
    body = {"username": 'TestUser',"password":"TestUser"}

    # api/certificate
    # link = "http://127.0.0.1:5000/api/certificate"
    # headers = {"Content-Type": "application/json",
    #            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjc3MTY0OSwianRpIjoiMzI2MmRjNzctNjAyZS00YzVhLThkNjEtMjBiZjM0NTdjNTgyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzA2NzcxNjQ5LCJjc3JmIjoiNGVjNDAzZDgtZGM0ZS00NDhmLTgxZmMtMDZmOWZmNzYyMjJkIiwiZXhwIjoxNzA2NzcyNTQ5fQ.ECqwLCT9rbwBYHmSUHmCFfMapXi2uoG6P9P2XLpBQP4"}
    # body = {"username": 'TestUser', "date": '2004-12-01', "type": "TestType"}


    # link = "http://127.0.0.1:5000/api/refresh"
    # headers = {"Content-Type": "application/json",
    #            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcwNjc3MjA0NSwianRpIjoiOGE3YjEzNzgtMmQ1MC00ZjNhLThiZWYtNDNhYmRhODNjYjVmIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOjEsIm5iZiI6MTcwNjc3MjA0NSwiY3NyZiI6IjUxYjEzNjQwLTcxZGItNDFjZS1hYzM4LTg0OWFmMTViOTU5NSIsImV4cCI6MTcwOTM2NDA0NX0.7S3fM7S8Pxz7FnZikTiI5Xt_R54ptjd5mca-WkLUvMU"}
    # body = {}

    received_response = requests.post(link, json=body, headers=headers)
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
