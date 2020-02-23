from flask import Flask, request, Response
from get import getMessagelist
from post import insertNewUser, insertNewChat, addNewMessage
from sentiment import getSentimentFromChat
import random
import json

app = Flask(__name__)


@app.route('/user/create/<username>', methods=['POST'])
# Crea usuario nuevo
def createUser(username):
    return insertNewUser(username)


@app.route('/chat/create', methods=['POST'])
# Crea chat nuevo
def createChat():
    name = request.args.get('chat_name')
    users = request.args.getlist('users')
    return insertNewChat(name, users)


@app.route('/chat/<chat_name>/addmessage', methods=['POST'])
# Añade un nuevo mensaje
def addMessage(chat_name):
    name = chat_name
    user = request.args.get('user')
    message = request.args.get('message')
    return addNewMessage(name, user, message)


@app.route('/chat/<chat_name>/list', methods=['GET'])
def messagesFromChat(chat_name):
    # Devuelve lista de mensajes de un chat
    return getMessagelist(chat_name)


@app.route('/chat/<chat_name>/sentiment', methods=['GET'])
def sentimentFromChat(chat_name):
    # Devuelve lista de mensajes de un chat
    return getSentimentFromChat(chat_name)


'''
- (GET) `/chat/<chat_id>/sentiment`
  - **Purpose:** Analyze messages from `chat_id`. Use `NLTK` sentiment analysis package for this task
  - **Returns:** json with all sentiments from messages in the chat
'''


app.run("0.0.0.0", 3000, debug=True)


# MIO

'''
@app.route('/newChat/', methods=['POST'])
def newChat():
    data = request.args.to_dict(flat=False)
    print(type(data), data)
    name = data["name"][0]
    contenido = data["content"][0]
    content = json.loads(contenido)
    return insertFullChat(name, content)
'''

# DE MARC
'''
@app.route('/company/<name>')
def getCompany(name):
    return getCompanyWithName(name)


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
