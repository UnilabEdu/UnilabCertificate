from src.models import User

from flask_restful import Resource, reqparse

from flask_login import current_user


# For test!
class AuthApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("name",
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

    def post(self):
        parser = self.parser.parse_args()
        new_user = User(name=parser["name"] ,password=parser["password"])
        new_user.create()
        return new_user.id, 200