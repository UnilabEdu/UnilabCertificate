from src.models import User

from flask_restful import Resource, reqparse

from flask_jwt_extended import create_access_token


# For test!
class AuthApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="Name is empty!")
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="Password is empty!")

    def get(self):
        all_users_id = User.query.all()
        users_json = []
        for user in all_users_id:
            user_id = {
                "id": user.id
            }
            users_json.append(user_id)
        return users_json, 200


class RegisterApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="Name is empty!")
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="Password is empty!")

    def post(self):
        parser = self.parser.parse_args()
        new_user = User(username=parser["username"], password=parser["password"])
        new_user.create()
        return new_user.id, 200


class LoginApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        required=True,
                        type=str)
    parser.add_argument("password",
                        required=True,
                        type=str)

    def post(self):
        received_args = self.parser.parse_args()
        user = User.query.filter(User.username == received_args["username"]).first()
        if not user:
            return "User not found! ", 404
        if user and user.check_pass(received_args['password']):
            token = create_access_token(identity=user.id)
            return token, 200
        else:
            return "Wrong password!", 400