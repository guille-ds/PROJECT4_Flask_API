from flask import Flask, request, Response
from src.get import getMessagelist, getUserMessages, recommendUser
from src.post import insertNewUser, insertNewChat, addNewMessage, insertFullChat
from src.sentiment import getSentimentFromChat
from src.recom import recommender
import random
import json


app = Flask(__name__)


@app.route('/user/create/<username>', methods=['POST'])
def createUser(username):
    # Crea usuario nuevo
    return insertNewUser(username)


@app.route('/chat/create', methods=['POST'])
def createChat():
    # Crea chat vacío nuevo
    name = request.args.get('chat_name')
    users = request.args.getlist('users')
    return insertNewChat(name, users)


@app.route('/chat/<chat_name>/addmessage', methods=['POST'])
def addMessage(chat_name):
    # Añade un nuevo mensaje a un chat existente
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
    # Devuelve lista de sentimientos de un chat
    return getSentimentFromChat(chat_name)


@app.route('/user/messages/<username>', methods=['GET'])
def userMessages(username):
    # Devuelve lista de mensajes de un usuario
    out = getUserMessages(username)
    docs = {}
    docs[username] = out
    claim = f'200 - All messages from {username} - messages = {docs}'
    print(claim)
    return out


@app.route('/recommend/<username>', methods=['GET'])
def recommend(username):
    # Devuelve usuarios recomendados para uno dado
    return recommendUser(username)


@app.route('/newChat/', methods=['POST'])
def importChat():
    # Recibe un diccionario anidado
    # Introduce un chat con nombre, usuarios y mensajes
    data = request.args.to_dict(flat=False)
    print(type(data), data)
    name = data["name"][0]
    contenido = data["content"][0]
    content = json.loads(contenido)
    return insertFullChat(name, content)


app.run("0.0.0.0", 3000, debug=True)
