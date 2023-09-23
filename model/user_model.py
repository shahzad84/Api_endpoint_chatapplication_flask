import mysql.connector
import json
from flask import make_response
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
        self.cur.execute("SELECT* FROM chat")
        result=self.cur.fetchall()
        if len(result)>0:
            return make_response({"payload":result},200)
        else:
            return make_response({"message":"No Data Found"},204)