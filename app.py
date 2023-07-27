from sanic import Sanic,response
from sanic.response import json
from database import db,Base,engine
from models import Login
from sqlalchemy.orm import Session


app = Sanic("__name__")
Base.metadata.create_all(engine)

@app.route("/user-register",methods=['POST'])
async def registerUser(request) :
    data = request.json
    UserId = data.get("UserId")
    Username = data.get("Username")
    Password = data.get("Password")
    user = Login(Username = Username, Password = Password )
    db.add(user)
    db.commit()
    return json({'message':"User Registred Successfully!!!"})

@app.route("/user-login",methods=['POST'])
async def loginUser(request) : 
    data = request.json
    Username = data.get("Username")
    Password = data.get("Password")

    if not Username or not Password :
        return response.json({'error' : 'Invalid Credentials'}, status=400)
    session = Session()
    user = session.query(Login).filter_by(Username=Username, Password=Password)
    session.close()

    if user :
         return response.json({'message':'Login Successfully'}, status=200)
    else : 
        return response.json({'error':'Invalid credentials'}, status=401)

if __name__ == '__main__': 
    app.run(host='0.0.0.0', port=8000)