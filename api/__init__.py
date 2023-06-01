from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_login import LoginManager
import config

app = Flask(__name__)
app.config.from_object(config.Config)
api = Api(app,prefix='/api/v1')
db = SQLAlchemy(app)
migrate = Migrate(app,db)
login_manager = LoginManager()
login_manager.init_app(app)
from .models import User
@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(int(user_id))

from .core.blueprint.login import login as login_blueprint
from .core.blueprint.registration import registration as registration_blueprint
from .core.blueprint.test import test as test_blueprint
from .core.blueprint.profil import profil_bp as profil_blueprint


app.register_blueprint(login_blueprint)
app.register_blueprint(registration_blueprint)
app.register_blueprint(test_blueprint)
app.register_blueprint(profil_blueprint)

from . import routes

