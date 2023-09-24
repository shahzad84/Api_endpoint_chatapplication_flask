from app import app
from flask import request
from model.user_model import user_model

import os
app.secret_key=os.urandom(24)
obj=user_model()

@app.route('/login', methods =['POST'])
def login():
    return obj.login()

@app.route("/register",methods=["POST"])
def register():
    return obj.register()

@app.route('/api/online-users/', methods=['GET'])
def get_online_users():
    return obj.get_online_users()