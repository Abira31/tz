from flask import Blueprint,render_template,redirect,session
from flask_login import current_user
from api.core.permission import is_admin
test = Blueprint('test',__name__)

@test.route("/test")
@is_admin()
def index():
    if not current_user.is_authenticated:
        return redirect("/")
    if not current_user.is_test:
        return render_template("test.html")
    return redirect("/profil")