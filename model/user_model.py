import mysql.connector
from flask import make_response, request
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

    def login(self):
        email=request.form.get("email")
        password=request.form.get("password")
        query = "SELECT * FROM chat WHERE email= %s AND password= %s "
        self.cur.execute(query,(email,password))
        result=self.cur.fetchall()
        if len(result)>0:
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
    