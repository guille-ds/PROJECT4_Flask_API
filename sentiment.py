from pymongo import MongoClient
from flask import Flask, request
import json
from textblob import TextBlob
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Connect to the database
client = MongoClient("mongodb://localhost:27017/apiflaskDB")
db = client.get_database()

sia = SentimentIntensityAnalyzer()
sentence = "I do not like you"
sia.polarity_scores(sentence)


def getSentimentFromChat(chatName):
    chatNames = db.chats.distinct("name")
    if chatName not in chatNames:
        out = ("Entered chat does not exist in the Database")
        print(out)
    else:
        chatMessages = db.messages.find({"chat_name": chatName})
        all = {}
        for m in chatMessages:
            mess = m['message']
            sentim = TextBlob(mess).sentiment
            print(sentim)
            sentim2 = sia.polarity_scores(mess)
            print(sentim2)
            all[mess] = sentim, sentim2
        out = json.dumps(all)
        print(out)
    return out
