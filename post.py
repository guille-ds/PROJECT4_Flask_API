from pymongo import MongoClient
from flask import Flask, request
from bson.json_util import dumps
import re

# Connect to the database
client = MongoClient("mongodb://localhost:27017/apiflaskDB")
db = client.get_database()

def getCompanyWithName(name):
    companies = client.get_default_database()["companies"]
    namereg = re.compile(name, re.IGNORECASE)
    print(namereg)
    query = companies.find_one({"name": namereg})
    if not query:
        raise ValueError("Company not found")
    return dumps(query)


def insertNewUser(name):
    users = db.users
    users.insert_one({"name": name}).inserted_id
    print('New user inserted')
    return 'Todo ok!'


def insertNewChat(name, x):
    # Crea un chat en la colección chats con nombre "name"
    chats = db.chats
    data = x
    #data = request.form.to_dict(x)
    print("data es", type(data))
    print("---------------------------------------")
    print(data)
    print("---------------------------------------")
    listUsers = [e for e in data.keys()]
    kind = ["Group_Chat" if len(listUsers) > 2 else "Two_Chat"][0]
    chats.insert_one({"name": name,
                      "type": kind,
                      "users": listUsers,
                      "content": data
                      }).inserted_id
    print('New chat inserted')
    return '200 - Todo ok'