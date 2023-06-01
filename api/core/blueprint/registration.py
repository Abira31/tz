from flask import Blueprint,render_template
from api.models import User

registration = Blueprint('registration',__name__)

@registration.route("/registration")
def regist():
    return render_template("registration.html")