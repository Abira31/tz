from flask_restful import Resource
from flask import request
from api import db
from api.models import User

class UserAPI(Resource):
    def put(self):
        user_db = db.session.query(User).get(int(request.json.get('user_id')))
        user_db.im = request.json.get('im')
        user_db.ot = request.json.get('ot')
        db.session.commit()
        return [],200