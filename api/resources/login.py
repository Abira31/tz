from flask_restful import Resource
from flask_login import login_user
from api import db
from api.models import User
from flask import request
from werkzeug.security import check_password_hash
class LoginAPI(Resource):
    def post(self):
        user = db.session.query(User).filter_by(fam=request.json.get('fam')).first()
        if user:
            if check_password_hash(user.password,request.json.get('password')):
                login_user(user)
                return [],200
        return [],204

