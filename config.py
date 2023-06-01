import pathlib
BASE_DIR = pathlib.Path(__file__).parent


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR/"data"/"db.sqlite3")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = '1234erfsdq2ewr324rwesdg34q4rt34w5'
    MEDIA = str(BASE_DIR)+'/media/'
