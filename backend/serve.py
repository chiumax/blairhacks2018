from flask import Flask
from flask import request
from passlib.hash import pbkdf2_sha512
from pymongo import MongoClient
from flask_cors import CORS, cross_origin
import requests
import uuid
import stocksoneel



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

@app.route('/login', methods=['POST'])
def login():
    if request.method=='POST':
        j=request.get_json(force=True)
        print(j)
        uname=j['uname']
        pw=j['pw']
        user = user_info.find_one({"uname": uname})
        if user:
            if pbkdf2_sha512.verify(pw,user["hashed_pw"]):
                response="success"
                user_id=uuid.uuid4().hex
                current_users.insert_one({"id":user_id,"uname":uname})
                return user_id
    return ""

@app.route('/buy', methods=['POST'])
def buy():
    if request.method=='POST':
        j=request.get_json(force=True)
        user_id=j["SessionID"]
        user=current_users.find_one({"id":user_id})
        buy_order=j['money']
        current_money=user["money"]
        if current_money<buy_order:
            return 'not enough money'
        stock_name=j["StockName"]
        stock_price = stocksoneel.getStock(stock_name)
        num_stocks=current_money/stock_price
        if not user["stocks"][stock_name]:
            user["stocks"][stock_name]=num_stocks
        else:
            user["stocks"][stock_name]+=num_stocks
        user["money"]=current_money-buy_order
        return 'success'

@app.route("/sell", methods=['POST'])
def sell():
    if request.method=='POST':
        j=request.get_json(force=True)
        user_id=j["SessionID"]
        user=current_users.find_one({"id":user_id})
        sell_order=j['num_stocks']
        current_money=user["money"]
        stock_name=j["StockName"]
        stock_price = stocksoneel.getStock(stock_name)
        if user["stocks"][stock_name]>=sell_order:
            user["money"]=current_money+sell_order*stock_price
            return 'success'
        return 'fail'

@app.route("/getMoney", methods=['POST'])
def getMoney():
    if request.method=='POST':
        user_id=j["SessionID"]
        user=current_users.find_one({"id":user_id})
        return user["money"]

@app.route("/getStocks", methods=['POST'])
def getStocks():
    if request.method=='POST':
        user_id=j["SessionID"]
        user=current_users.find_one({"id":user_id})
        return user["stocks"]

@app.route("/search", methods=['POST'])
def stock_search():
    if request.method=='POST':
        j=request.get_json(force=True)
        query=j['query']
        our_base="localhost:3000/stock/"
        base="https://www.nasdaq.com/symbol/?Load=true&Search="
        r=requests.get(base+query)
        out=r.text
        first='<div id="SymbolLookupContainer" class="genTable">'
        start="</tr>"
        end='</div><!--end genTable-->'
        f_ind=out.find(first)
        st_ind = out.find(start, f_ind)
        end_ind = out.find(end,st_ind)
        interesting_stuff = out[st_ind+20:end_ind-150]

        l=interesting_stuff.split("a href=")
        l2=[]
        names=[]
        d=dict()
        for i in range(0,len(l),2):
            start=l[i].find('">')
            end=l[i].find("</a>",start)
            names.append(l[i][start+2:end])
        for i in range(1, len(l), 2):
            end=l[i].find('">')
            end2=l[i].find("</a>",end)
            l[i]=l[i].replace("  ","")
            a=l[i][end-(end2-end-2):end]
            d[names[i//2+1]]=a
        return str(d).replace("'",'"')
@app.route('/stock/<stock_name>/<interval>')
def stock_prices(stock_name, interval):
    return stocksoneel.getStockHistory(stock_name,interval)

@app.route('/crypto/<coin_name>/<interval>')
def coin_prices(coin_name, interval):
    return stocksoneel.getCryptoHistory(coin_name,interval)
