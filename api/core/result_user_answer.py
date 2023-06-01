from flask_login import current_user
from api import db
from api.models import UserAnswer
from collections import OrderedDict
from sqlalchemy.orm import join
from api.models import Test,Answer as Answer_md
class Answer():
    def get_answer(self):
        return db.session.query(UserAnswer).filter_by(user_id=current_user.id).all()

class Table():
    def __init__(self,answer:list[UserAnswer]):
        self.answer = answer
        self.table = []
    def create(self):
        for answer in self.answer:
            self.insert(answer)
        return self.table
    def insert(self,answer):
        table_ord = OrderedDict()
        right = set()
        user_answer = set()
        is_right = set()
        for ans in answer.answer:
            test = ans.test_answer[0]
            table_ord['test_text'] = test.text
            is_right.add(ans.is_right)
            answers_right = db.session.query(Answer_md).select_from(join(Answer_md,Test,Test.answer))\
                .filter(Answer_md.is_right==True,Test.id==test.id).all()
            for ans_right in answers_right:
                right.add(ans_right.text)
            table_ord['test_right'] = ', '.join(right)
            user_answer.add(ans.text)
        table_ord['user_answer'] = ', '.join(user_answer)
        table_ord['is_right'] = True if is_right == {True} else False
        self.table.append(table_ord)

class ResultTest:
    @staticmethod
    def result():
        answer = Answer()
        result_answer = answer.get_answer()
        table = Table(result_answer)
        return table.create()


