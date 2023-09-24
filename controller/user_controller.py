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

@app.route('/logout')
def logout():
    return obj.logout()

@app.route('/api/chat/start/',methods=["POST"])
def start_chat():
    recipient_id = request.form.get("recipient_id")
    return obj.start_chat(recipient_id)

@app.route('/api/suggested-friends/<int:id>', methods=['GET'])
def get_suggested_friends(id):  
    return obj.get_suggested_friends(id)