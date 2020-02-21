from flask import Flask, request
from post import getCompanyWithName, insertNewUser, insertNewChat
import random
import json

app = Flask(__name__)


@app.route('/newChat/')
def newChat():
    print(type(request),request)
    data = request.args.to_dict(flat=False)
    name = data["name"][0]
    print(type(data),data)
    contenido = data["content"][0]
    res = json.loads(contenido) 
    print(type(res),res)
    return insertNewChat(name, res)

@app.route('/newUser/<name>')
def newUser(name):
    return insertNewUser(name)

@app.route('/')
def hello():
    pepe = {
        "nombre": "Luis",
        "edad": 30
    }
    return pepe

@app.route('/company/<name>')
def getCompany(name):
    return getCompanyWithName(name)

app.run("0.0.0.0", 3000, debug=True)








'''
def controllerFn(): return {"hola": "pepe"}


app.route('/hola')(controllerFn)


@app.route('/ta')
def taChooser():
    return random.choice(tas)


@app.route('/ta/<name>')
def taChooserWithName(name):
    print(f"Getting TA data for {name}")
    return queryTas(name)


@app.route('/homer')
def homer():
    return """
    <img src="https://www.grupoblc.com/wp-content/uploads/2013/10/images_curiosita_homer.jpg">
    """
'''