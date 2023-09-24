import mysql.connector
from flask import jsonify, make_response, request,session
import re
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
        
