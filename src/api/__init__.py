from flask_restful import Api

from src.api.auth.endpoints import AuthApi, RegisterApi, LoginApi
from src.api.certificate.endpoints import CertificateApi, GetCertificateApi


api = Api()

# For test!
api.add_resource(AuthApi, "/users_id")
api.add_resource(RegisterApi, "/api/register")
api.add_resource(LoginApi, "/api/login")
api.add_resource(CertificateApi, "/api/certificate")
api.add_resource(GetCertificateApi, "/api/get_certificate")
