from flask_restful import Resource
from api import db
from api.models import User
from flask import request

class RegistrationAPI(Resource):
    def post(self):
        user = db.session.query(User).filter_by(fam=request.json.get('fam')).first()
        if not user:
            user_db = User(**request.json)
            db.session.add(user_db)
            db.session.commit()
            return [],201
        return [],400