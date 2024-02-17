from flask_restful import Resource, reqparse

from datetime import datetime

import uuid

from flask_jwt_extended import jwt_required

from src.models.certificate import Certificate
from src.models.users import User

from src.utils import certificate_2d

from werkzeug.datastructures import FileStorage

from src.config import Config

from os import path


class CertificateApi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="Username is empty!")
    parser.add_argument("date",
                        type=str,
                        required=True,
                        help="Date is empty!")
    parser.add_argument("generate_date",
                        type=str,
                        default=lambda: datetime.now().strftime('%Y-%m-%d'))

    parser.add_argument("type",
                        type=str,
                        required=True,
                        help="Date is empty!")
    parser.add_argument("subject",
                        type=str,
                        required=True,
                        help="Date is empty!")

    @jwt_required()
    def post(self):
        parser = self.parser.parse_args()
        date_obj = datetime.strptime(parser["date"], "%Y-%m-%d").date()
        generate_date_obj = datetime.strptime(parser["generate_date"], "%Y-%m-%d").date()
        new_certificate = Certificate(username=parser["username"],
                                      date=date_obj,
                                      generate_date=generate_date_obj,
                                      type=parser["type"],
                                      uuid=str(uuid.uuid4()),
                                      subject=parser["subject"]
                                      )
        new_certificate.create()
        certificate_2d(new_certificate.username, new_certificate.type, new_certificate.subject,
                       str(new_certificate.date)[0:4])
        return new_certificate.uuid, 200


class GetCertificateApi(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("uuid",
                        type=str,
                        required=True)

    def get(self):
        parser = self.parser.parse_args()
        certificate_uu_id = parser["uuid"]
        certificate = Certificate.query.filter_by(uuid=certificate_uu_id).first()
        certificate_data = {
            "id": certificate.id,
            "username": certificate.username,
            "date": certificate.date.strftime("%Y-%m-%d"),
            "generate_date": certificate.generate_date.strftime("%Y-%m-%d"),
            "type": certificate.type,
            "uuid": certificate.uuid
        }
        return certificate_data, 200


class SignatureApi(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("user_id",
                        type=int,
                        location="form",
                        required=True,
                        help='Id is empty')

    parser.add_argument('picture',
                        type=FileStorage,
                        location='files',
                        required=True,
                        help="Picture is empty")

    @jwt_required()
    def post(self):
        parser = self.parser.parse_args()
        
        user_id = parser["user_id"]
        user = User.query.filter_by(id=user_id).first()

        picture = parser['picture']
        picture_name = str(uuid.uuid4())

        user.signature = picture_name

        picture_location = path.join(Config.BASE_DIRECTORY, "assets", "signatures", f'{picture_name}.png')
        picture.save(picture_location)
