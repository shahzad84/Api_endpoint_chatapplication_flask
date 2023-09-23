import mysql.connector
class user_model():
    def __init__(self):
        try:
            con=mysql.connector.connect(host="localhost",user="root",password="password",database="chatflask",port=1080)
            print("connected_________!")
        except:
            print("__some error")
    def login(self):
        return "hii this is model"