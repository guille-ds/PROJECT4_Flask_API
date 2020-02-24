from pymongo import MongoClient
from flask import Flask, request
from bson.json_util import dumps

# Connect to the database
client = MongoClient("mongodb://localhost:27017/apiflaskDB")
db = client.get_database()


def insertNewUser(name):
    # Inserta un nuevo usuario en la colección "users"
    users = db.users
    userNames = users.distinct("name")
    if name in userNames:
        claim = ("User already exist")
        print(claim)
    else:
        r = users.insert_one({"name": name}).inserted_id
        claim = f'200 - New user {name} inserted succesfully - user_id = {r}'
        print(claim)
    return claim


def insertNewChat(name, arrayUsers):
    # Inserta un nuevo chat vacío en la colección "chats"
    chat = db.chats
    chatNames = chat.distinct("name")
    if name in chatNames:
        claim = ("Chat already exist")
        print(claim)
    else:
        kind = ["Group_Chat" if len(arrayUsers) > 2 else "Two_Chat"][0]
        r = chat.insert_one({"kind": kind,
                             "name": name,
                             "users": arrayUsers}).inserted_id
        claim = f'200 - New chat "{name}" inserted succesfully - chat_id = {r}'
        print(claim)
    return claim


def addNewMessage(name, user, message):
    # Inserta un nuevo mensaje en el chat con nombre "name" si el usuario pertenece al chat
    chatUsers = db.chats.find_one({"name": name})["users"]
    if user not in chatUsers:
        claim = ("User is not part of the chat")
        print(claim)
    else:
        messages = db.messages
        r = messages.insert_one({"chat_name": name,
                                 "user": user,
                                 "message": message}).inserted_id
        claim = f'200 - New message "{message}" inserted succesfully - message_id = {r}'
        print(claim)
    return claim


def insertFullChat(name, contenido):
    # Crea un chat en la colección "chats" con nombre "name" y con todos sus mensajes.
    # Cuenta el número de usuarios y establece el tipo de chat en función de ello.
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
