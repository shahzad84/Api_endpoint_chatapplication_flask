from app import app
from flask import request
from model.user_model import user_model
obj=user_model()
@app.route("/login")
def login():
    return obj.login()
