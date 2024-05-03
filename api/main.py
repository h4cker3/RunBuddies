from flask import Flask, request, render_template, redirect, jsonify
from data import db_session
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
import json
from data.users import Users
from data.trophies import Trophies

app = Flask(__name__)
app.config['SECRET_KEY'] = 'SECRET KEY FROM ME'
VERSION = 'v0.1alpha'

db_session.global_init("db/base.db")

login_manager = LoginManager()
login_manager.init_app(app)

STATUS = "WORKING (FINE)"


@app.route("/api")
def index():
    return jsonify({"version": VERSION,
                    "status": STATUS})


@app.route("/api/user/<int:id>")
def data_user(id):
    db_sess = db_session.create_session()
    user = db_sess.query(Users).get(id)
    if not user:
        return jsonify({"code": -1})
    rate = -user.penalty
    for elem in json.loads(user.trophies):
        rate += db_sess.query(Trophies).get(elem).rate
    db_sess.close()
    return jsonify({"code": 0, "name": user.name, "rate": rate, "link": user.link, "bio": json.loads(user.bio)})


if __name__ == "__main__":
    app.run()
