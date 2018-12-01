from flask import Flask, request
from passlib.hash import pkbdf2_sha512
from pymongo import MongoClient

c = MongoClient('localhost',27017)
db=c.test
user_info=c.user_info

app = Flask.app(__name__)

@app.route('/register')
def register():
    if request.method=='POST':
        uname=request.args.get('uname')
        pw=request.args.get('pw')
        hash=pkbdf2_sha512.hash(pw)
        entry={"uname":uname, "hashed_pw":hash}

@app.route('/login')
def login():
    if requests.method=='POST':
        uname=request.args.get('uname')
        pw=request.args.get('pw')
        user = user_info.find_one({"uname": uname})
        if user:
            if pkbdf2_sha512.verify(pw,user["hash"]):
                return "Success"
    return "Fail"
