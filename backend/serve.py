from flask import Flask
from flask import request
from passlib.hash import pbkdf2_sha512
from pymongo import MongoClient
from flask_cors import CORS, cross_origin




c = MongoClient('localhost',27017)
db = c.test
user_info = db.user_info
current_users = db.loggedin_users

app = Flask(__name__)
CORS(app)
@app.route("/")
def hello():
    return "Hello, World!"
@app.route('/register', methods=['POST'])
def register():
    if request.method=='POST':
        j=request.get_json(force=True)
        uname=j['uname']
        pw=j['pw']
        print(uname, pw)
        h=pbkdf2_sha512.hash(pw.encode())
        entry={"uname":uname, "hashed_pw":h, "money": 10000, "stocks":{}}
        user_info.insert_one(entry)
        return 'success'

@app.route('/login')
def login():
    if requests.method=='POST':
        j=request.json()
        print(j)
        uname=request.args.get('uname')
        pw=request.args.get('pw')
        user = user_info.find_one({"uname": uname})
        if user:
            if pbkdf2_sha512.verify(pw,user["hash"]):
                response="success"
                user_id=uuid.uuid4().hex()
                current_users.insert_one({"id":user_id,"uname":uname})
                response.set_cookie("SessionID", userid)
                return response
    return "fail"

@app.route('/buy')
def buy():
    if request.method=='POST':
        user_id=request.cookies.get("SessionID")
        user=current_users.find_one({"id":user_id})
        buy_order=request.args.get('money')
        current_money=user["money"]
        if current_money<buy_order:
            return 'not enough money'
        stock_name=request.args.get("StockName")
        stock_price = 1000 #TODO: Stock Price Function
        num_stocks=current_money/stock_price
        if not user["stocks"][stock_name]:
            user["stocks"][stock_name]=num_stocks
        else:
            user["stocks"][stock_name]+=num_stocks
        user["money"]=current_money-buy_order
        return 'success'

@app.route("/sell")
def sell():
    if request.method=='POST':
        user_id=request.cookies.get("SessionID")
        user=current_users.find_one({"id":user_id})
        sell_order=request.args.get('num_stocks')
        current_money=user["money"]
        stock_name=request.args.get("StockName")
        stock_price = 1000 #TODO: Stock Price Function
        if user["stocks"][stock_name]>=sell_order:
            user["money"]=current_money+sell_order*stock_price
            return 'success'
        return 'fail'

@app.route("/getMoney")
def getMoney():
    if request.method=='POST':
        user_id=request.cookies.get("SessionID")
        user=current_users.find_one({"id":user_id})
        return user["money"]
        
@app.route("/getStocks")
def getStocks():
    if request.method=='POST':
        user_id=request.cookies.get("SessionID")
        user=current_users.find_one({"id":user_id})
        return user["stocks"]
