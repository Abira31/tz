from . import db
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

test_answer = db.Table(
    'test_answer',
    db.Column('test_id', db.Integer, db.ForeignKey('test.id'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id'), primary_key=True)
)

user_answer = db.Table(
    'test_user_answer',
    db.Column('user_id', db.Integer, db.ForeignKey('user_answers.id'), primary_key=True),
    db.Column('answer_id', db.Integer, db.ForeignKey('answer.id'), primary_key=True)
)


class User(db.Model,UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    fam = db.Column(db.String(120), nullable=False, unique=True)
    im = db.Column(db.String(120), nullable=False)
    ot = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(15),nullable=False)
    answer = db.relationship('UserAnswer', backref='user', lazy=True)
    is_test = db.Column(db.Boolean, nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False)

    def __init__(self,fam,im,ot,password,is_test=False,is_admin=False):
        self.fam = fam
        self.im = im
        self.ot = ot
        self.password = generate_password_hash(password)
        self.is_test = is_test
        self.is_admin = is_admin



class Test(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(120), nullable=False, unique=True)
    answer = db.relationship('Answer', secondary=test_answer, lazy='subquery',backref=db.backref('test_answer', lazy=True))
    is_many_answer = db.Column(db.Boolean, nullable=False)
    test = db.relationship("UserAnswer", backref="test", lazy='dynamic')
    def __init__(self,text,answer=None,is_many_answer=False):
        self.text = text
        if not answer:
            self.answer = []
        else:
            self.answer = answer
        self.is_many_answer = is_many_answer

class Answer(db.Model):
    __tablename__ = 'answer'
    id = db.Column(db.Integer, primary_key=True)
    num = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(120), nullable=False)
    is_right = db.Column(db.Boolean, nullable=False)

    def __init__(self,num,text,is_right=False):
        self.num = num
        self.text = text
        self.is_right=is_right


class UserAnswer(db.Model):
    __tablename__ = 'user_answers'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    test_id = db.Column(db.Integer, db.ForeignKey("test.id"))
    answer = db.relationship('Answer', secondary=user_answer, lazy='subquery',
                              backref=db.backref('user_resumes', lazy=True))
    is_right = db.Column(db.Boolean, nullable=False)
    def __init__(self,user_id,test_id,answer=None,is_right=False):
        self.user_id = user_id
        self.test_id = test_id
        if not answer:
            self.answer = []
        else:
            self.answer = answer
        self.is_right = is_right



