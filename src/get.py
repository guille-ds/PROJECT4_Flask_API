from pymongo import MongoClient
from flask import Flask, request
import json
from src.recom import recommender

# Connect to the database
client = MongoClient("mongodb://localhost:27017/apiflaskDB")
db = client.get_database()


def getMessagelist(name):
    # Devuelve todos los mensajes de un chat
    chatNames = db.chats.distinct("name")
    if name not in chatNames:
        claim = ("Entered chat does not exist in the Database")
        print(claim)
    else:
        r = [x["message"] for x in db.messages.find({"chat_name": name})]
        claim = f'200 - "{name}" chat found - messages = {r}'
        print(claim)
    return claim


def getUserMessages(username):
    # Devuelve todos los mensajes de un usuario
    userNames = db.users.distinct("name")
    if username not in userNames:
        claim = f"Entered user {username} does not exist in the Database"
        print(claim)
    else:
        messages = [x["message"] for x in db.messages.find({"user": username})]
        mess = " ".join(messages)
        claim = mess
    return claim


def recommendUser(username):
    # Devuelve un usuario recomendado
    userNames = db.users.distinct("name")
    docs={}
    if username not in userNames:
        claim = f"Entered user {username} does not exist in the Database"
        print(claim)
    else:
        for e in userNames:
            docs[e]=getUserMessages(e)
        here = recommender(username, docs)
        
        claim = docs
        print(claim)
    return here


    
