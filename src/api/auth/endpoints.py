from src.models import User

from flask_restful import Resource, reqparse

from flask_login import current_user


# For test!
class AuthApi(Resource):

    def get(self):
        all_users_id = User.query.all()
        users_json = []
        for user in all_users_id:
            user_id = {
                "id": user.id
            }
            users_json.append(user_id)
        return users_json, 200
