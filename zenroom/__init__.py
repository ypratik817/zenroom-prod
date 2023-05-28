from flask import Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '5ShWn8iqyeYU2imQHtCRT3BlbkFJXvKvaV0i313dBwgigKTdWtj@161107'
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"
bcrypt = Bcrypt(app)

from zenroom import routes