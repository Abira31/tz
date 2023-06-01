from flask import Blueprint,render_template
from flask_login import logout_user
login = Blueprint('login',__name__)

@login.route("/")
def index():
    logout_user()
    return render_template("index.html")