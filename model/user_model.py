import mysql.connector
from flask import make_response, request
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
            return make_response({"message":"login sucessfull"},201)
        else:
            return make_response({"message":"Invalid email or password"},201)
        

    