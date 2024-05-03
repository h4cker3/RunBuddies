from flask import Flask, request, render_template, redirect, jsonify
from data import db_session
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
import json
from data.users import Users
from data.trophies import Trophies

base_json_post = {"name": "Zaharov", "email": "ilovevova@mail.com", "password": "helpme", "bio": {"age": 16}}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'adbre'
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
        db_sess.close()
        return jsonify({"code": -1})
    rate = -user.penalty
    for elem in json.loads(user.trophies):
        rate += db_sess.query(Trophies).get(elem).rate
    db_sess.close()
    return jsonify({"code": 0, "name": user.name, "rate": rate, "link": user.link, "bio": json.loads(user.bio),
                    "trophies": json.loads(user.trophies), "events": json.loads(user.events)})


@app.route("/api/check_pass/<string:email>/<string:password>")
def check_pass(email, password):
    db_sess = db_session.create_session()
    user = db_sess.query(Users).filter(email=email)
    db_sess.close()
    if not user:
        return jsonify({"code": -1})
    if user.password == password:
        return jsonify({"code": 0, "id": user.id, "name": user.name})
    else:
        return jsonify({"code": -1})


@app.route("/api/add_user/<string:api_key>", methods=["POST"])
def add_user(api_key):
    if api_key != app.config["SECRET_KEY"]:
        return jsonify({"code": -1})
    if not request.json:
        return jsonify({"code": -1})
    db_sess = db_session.create_session()
    if len(db_sess.query(Users).filter(Users.email == request.json['email']).all()):
        db_sess.close()
        return {jsonify({"code": -1})}
    user = Users(email=request.json['email'],
                 name=request.json['name'],
                 password=request.json['password'],
                 bio=json.dumps(request.json['bio']))
    db_sess.add(user)
    db_sess.commit()
    db_sess.close()
    return {"code": 0, "id": user.id}


if __name__ == "__main__":
    app.run()
