from flask_restful import Resource, reqparse

from datetime import datetime

import uuid

from flask_jwt_extended import jwt_required

from src.models.certificate import Certificate


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

    @jwt_required()
    def post(self):
        parser = self.parser.parse_args()
        date_obj = datetime.strptime(parser["date"], "%Y-%m-%d").date()
        generate_date_obj = datetime.strptime(parser["generate_date"], "%Y-%m-%d").date()
        new_certificate = Certificate(username=parser["username"],
                                      date=date_obj,
                                      generate_date=generate_date_obj,
                                      type=parser["type"],
                                      uuid=str(uuid.uuid4()))
        new_certificate.create()
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