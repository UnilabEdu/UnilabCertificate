from src.models import User

from flask_restful import Resource, reqparse

from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity


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
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            response_data = {
                'access_token': access_token,
                'refresh_token': refresh_token
            }
            return response_data, 200
        else:
            return "Wrong password!", 400


class RefreshApi(Resource):
    @jwt_required(refresh=True)
    def post(self):
        logged_user = get_jwt_identity()
        print(logged_user)
        new_access_token = create_access_token(identity=logged_user)
        return new_access_token, 200
