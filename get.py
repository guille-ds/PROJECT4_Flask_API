from pymongo import MongoClient
from flask import Flask, request

# Connect to the database
client = MongoClient("mongodb://localhost:27017/apiflaskDB")
db = client.get_database()
'''
- (GET) `/chat/<chat_id>/list`
  - **Purpose:** Get all messages from `chat_id`
  - **Returns:** json array with all messages from this `chat_id`
'''

def getMessagelist(name):
    chatNames = db.chats.distinct("name")
    if name not in chatNames:
        claim = ("There is no chat called with that name")
        print(claim)
    else:
        r = [x["message"] for x in db.messages.find({"chat_name":name})]
        claim = f'200 - "{name}" chat found - message_id = {r}'
        print(claim)
    return claim


