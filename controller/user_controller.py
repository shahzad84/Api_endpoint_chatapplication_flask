from app import app
from flask import request
from model.user_model import user_model
obj=user_model()

@app.route('/login', methods =['POST'])
def login():
    return obj.login()

@app.route("/register",methods=["POST"])
def register():
    return obj.register()
