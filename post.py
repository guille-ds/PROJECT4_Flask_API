from pymongo import MongoClient
from flask import Flask, request
from bson.json_util import dumps
import re

# Connect to the database
client = MongoClient("mongodb://localhost:27017/apiflaskDB")
db = client.get_database()


def insertNewUser(name):
    # Inserta un nuevo usuario en la colección "users"
    users = db.users
    r = users.insert_one({"name": name}).inserted_id
    #res = db.test.find_one({"name": name})
    claim = f'200 - New user {name} inserted succesfully - user_id = {r}'
    print(claim)
    return claim


def insertNewChat(name, arrayUsers, messages):
    # Inserta un nuevo chat en la colección "chats"
    chat = db.chats
    kind = ["Group_Chat" if len(arrayUsers) > 2 else "Two_Chat"][0]
    r = chat.insert_one({"kind": kind,
                         "name": name,
                         "users": arrayUsers,
                         "messages": messages}).inserted_id
    claim = f'200 - New chat "{name}" inserted succesfully - chat_id = {r}'
    print(claim)
    return claim


def addNewMessage(name, user, message):
    # Inserta un nuevo mensaje en el chat con nombre "name" si el usuario pertenece al chat
    chatUsers = db.chats.find_one({"name": name})["users"]
    if user not in chatUsers:
        claim = ("User is not part the chat")
        print(claim)
    else:
        messages = db.messages
        r = messages.insert_one({"chat_name": name,
                                 "user": user,
                                 "message": message}).inserted_id
        claim = f'200 - New message "{message}" inserted succesfully - message_id = {r}'
        print(claim)
    return claim


'''
def insertFullChat(name, contenido):
    # Crea un chat en la colección "chats" con nombre "name"
    chats = db.chats
    listUsers = [e for e in contenido.keys()]
    kind = ["Group_Chat" if len(listUsers) > 2 else "Two_Chat"][0]
    chats.insert_one({"name": name,
                      "kind": kind,
                      "users": listUsers,
                      "content": contenido
                      }).inserted_id
    claim = '200 - Todo ok - New chat inserted succesfully'
    print(claim)
    return claim

def getCompanyWithName(name):
    companies = client.get_default_database()["companies"]
    namereg = re.compile(name, re.IGNORECASE)
    print(namereg)
    query = companies.find_one({"name": namereg})
    if not query:
        raise ValueError("Company not found")
    return dumps(query)
'''
