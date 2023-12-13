from flask_restful import Api

from src.api.auth.endpoints import AuthApi, RegisterApi, LoginApi


api = Api()

# For test!
api.add_resource(AuthApi, "/users_id")
api.add_resource(RegisterApi, "/api/register")
api.add_resource(LoginApi, "/api/login")
