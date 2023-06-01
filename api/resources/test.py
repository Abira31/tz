from flask_restful import Resource
from flask import jsonify,make_response,request
from flask_login import current_user
from sqlalchemy.orm import join
from api import db
from api.models import Test,Answer,UserAnswer
from api.schemas.test import TestBaseModel

class TestAPI(Resource):
    def get(self):
        tests_db = db.session.query(Test).order_by(Test.id.asc()).all()
        tests = [TestBaseModel.from_orm(test) for test in tests_db]
        response = make_response(
            jsonify([test.dict() for test in tests]),
            200,
        )
        response.headers["Content-Type"] = "application/json"
        return response

    def post(self):
        if not current_user.is_test:
            results = request.json
            for result in results:
                answer = db.session.query(Answer).filter(Answer.id.in_(result.get('answer')),Answer.is_right==True).all()
                user_answer = UserAnswer(
                    user_id = current_user.id,
                    test_id = db.session.query(Test).get(result.get('test_id')).id
                )

                if len(answer) != 0:
                    if len(result.get('answer')) == len(answer):
                        user_answer.is_right = True
                db.session.add(user_answer)
                db.session.commit()
                user_answer.answer = db.session.query(Answer).filter(Answer.id.in_(result.get('answer'))).all()
                current_user.is_test = True
                db.session.commit()

        return [],201