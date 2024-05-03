from flask import Flask, request, render_template, redirect, jsonify
from data import db_session
from datetime import datetime
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user
import json

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
                    "message": "HELLO! NEW USER!",
                    "status": STATUS})
