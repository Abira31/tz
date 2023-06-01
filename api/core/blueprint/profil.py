from flask import Blueprint,render_template,redirect,send_file
from flask_login import logout_user,current_user
from api.core.result_user_answer import ResultTest
from api.core.create_report import CreateFileExcel

profil_bp = Blueprint('profil',__name__)

@profil_bp.route("/profil")
def profil():
    if not current_user.is_authenticated:
        return redirect("/")
    result = ResultTest.result()
    # report = CreateFileExcel()
    # path = report.create()
    return render_template("profil.html",user=current_user,result=result)

@profil_bp.route("/profil/exits")
def exits():
    logout_user()
    return redirect("/")

@profil_bp.route("/profil/download_file")
def download_file():
    report = CreateFileExcel()
    path = report.create()
    return send_file(path, as_attachment=True)