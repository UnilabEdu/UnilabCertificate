from flask_restful import Api
from src.api.auth.endpoints import AuthApi


api = Api()

# For test!
api.add_resource(AuthApi, "/users_id")