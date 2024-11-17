import json
import os

def load_user():
    if os.path.exists('data/users.json'):
        with open('data/users.json','r')as filename:
            return json.load(filename)
    else:
        return []

def save_user(user_data):
    with open('data/users.json','w')as filename:
        json.dump(user_data,filename)

def load_course():
    if os.path.exists('data/courses.json'):
        with open('data/courses.json','r')as filename:
            return json.load(filename)
    else:
        return []

def save_course(course_data):
    with open('data/courses.json','w')as filename:
        json.dump(course_data,filename)

