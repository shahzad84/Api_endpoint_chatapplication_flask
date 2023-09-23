from app import app
from model.user_model import user_model
obj=user_model()
@app.route("/login")
def login():
    return obj.login()
