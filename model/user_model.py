import mysql.connector
from flask import jsonify, make_response, request,session,Flask
import re
import json

class user_model():
    def __init__(self):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="password",database="chatflask",port=1080)
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connected_________!")
        except:
            print("__some error")

    def set_user_online(self,id):
        query = "UPDATE chat SET online = 1 WHERE id =%s"
        self.cur.execute(query,(id, ))
    

    def set_user_offline(self,id):
        query = "UPDATE chat SET online = 0 WHERE id =%s"
        self.cur.execute(query,(id,))

    def login(self):
        email=request.form.get("email")
        password=request.form.get("password")
        query = "SELECT * FROM chat WHERE email= %s AND password= %s "
        self.cur.execute(query,(email,password))
        result=self.cur.fetchall()
        if result:
            if len(result) > 0:
                first_result = result[0]
                self.set_user_online(first_result["id"])
                session['loggedin'] = True
                session["id"]=first_result["id"]
                session["name"]=first_result["name"]
                return make_response({"message":"login sucessfull"},200)
        else:
            return make_response({"message":"Invalid email or password"},201)

    def register(self):
        name=request.form.get("name")
        email=request.form.get("email")
        password=request.form.get("password")
        hiquery ='SELECT * FROM chat WHERE name= %s'
        self.cur.execute(hiquery,(name, ))
        account = self.cur.fetchall()
        if account:
            return make_response({"message":"account already exist"},201)
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            return make_response({"message":"Invalid email "},201)
        elif not re.match(r'[A-Za-z0-9]+', name):
            return make_response({"message":"name should only contain character and number"},201)
        elif not name or not password or not email:
            return make_response({"message":"please fill form"},201)
        else:
            query ='INSERT INTO chat VALUES (NULL, %s, %s, %s)'
            self.cur.execute(query,(name, email, password, ))
            return "registered"
        
    def get_online_users(self):

        if 'id' not in session:
            return make_response({"message":"user not loged in"},201)
        query = "SELECT * FROM chat WHERE online= 1"
        self.cur.execute(query)
        online_users = self.cur.fetchall()
        if len(online_users)>0:
           return jsonify(online_users)
        else:
            return make_response({"message":"all users are offline"},201)
        
    def logout(self):
        id = session.get('id')
        if id:
            self.set_user_offline(id)
            session.pop('loggedin', None)
            session.pop('id', None)
            session.pop('username', None)
            return make_response({"message":"logout successful"},201)
        else:
           return make_response({"message":"please login"},201)
        
    def is_user_online(self, id):
        query = "SELECT online FROM chat WHERE id = %s"
        self.cur.execute(query, (id,))
        result = self.cur.fetchone()
        if result and result["online"] == 1:
            return True
        else:
            return False 
        
    def start_chat(self,recipient_id):
        if 'id' not in session:
            return make_response({"message": "User not logged in"}, 401)
        sender_id = session['id']
        recipient_online = self.is_user_online(recipient_id)
        if recipient_online:
            chat_session_query = "INSERT INTO chat_session (sender_id,recipient_id) VALUES (%s, %s)"
            try:
                self.cur.execute(chat_session_query, (sender_id,recipient_id,))
                return make_response({"message": "Chat started with recipient"}, 200)
            except Exception as e:
                self.login.error(f"Error starting chat: {str(e)}")
                return make_response({"error": "Chat initiation failed"}, 500)
        else:
            return make_response({"message": "Recipient is offline or unavailable"}, 404)
        
    def get_suggested_friends(self,id):
        try:
            with open('users.json', 'r') as file:
                friends_data = json.load(file)
            user = next((u for u in friends_data.get("users", []) if u.get("id") == id), None)
            if user:
                recommended_friends = user.get("recommended_friends", [])
                return jsonify({"recommended_friends": recommended_friends})
            else:
                return jsonify({"error": "User not found"}), 404
        except Exception as e:
            return jsonify({"error": str(e)}), 500