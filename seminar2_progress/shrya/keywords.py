# -*- coding: utf-8 -*-
"""
@author: Shubhadeep
"""
bot = "VIKI-Bot: "
user = "Anonymous: " 

# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up","hey","hii")

GREETING_RESPONSES = ["'sup bro", "Hey", "Hello", "Hi"]

add_on_greet = ", my name is VIKI-Bot. You can consult me for MSIT-related queries!"

user_name = "Anonymous"

def upd_user(name):
    global user
    global user_name
    user_name = name
    user = user_name + ": "


# Sentences we'll respond with if the user greeted us farewell
FAREWELL_KEYWORDS = ("bye", "sayonara", "astalavista", "farewell")

FAREWELL_RESPONSES = ["Bye", "Farewell", "See you later", "Sayonara"]

add_on_farewell = "! Hope I was of some help to you"


# asking user_name
ASK_USERNAME = ("May I know your name?", "What is your good name?")
