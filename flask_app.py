from flask import Flask,render_template,jsonify,request,make_response
import mysql.connector
import cv2
import base64
import io
import numpy as np
from flask_ngrok import run_with_ngrok

qr_status=amount=-1

app = Flask('__name__',template_folder='template')
#run_with_ngrok(app)


def db():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bintech"
    )
    myc = mydb.cursor()
    return mydb,myc


def Login(user,pwd):
    mydb,myc = db()
    nameq = "select name from auth"
    name_list = []
    name = user
    password = pwd
    check = f"select * from auth where name='{name}'"
    myc.execute(nameq)
    for i in myc:
        for j in i:
            name_list.append(j)

    if name in name_list:
        myc.execute(check)
        for i in myc:
            pass_check = i[2]
        if password == pass_check:
            print('Login successful')
            return 1
        else:
            return "password incorrect"
    else:
        return "User not found"
    

def Register(name,mail,pwd):
    mydb,myc = db()
    nameq = "select name from auth"
    name_list = []
    add = "insert auth (name,email,password) values(%s,%s,%s)"
    val = (name,mail,pwd)
    myc.execute(nameq)
    for i in myc:
        for j in i:
            name_list.append(j)

    if name in name_list:
        return (f"{name} user already exist")
    else:
        myc.execute(add,val)
        mydb.commit()
        return 1

def qr_scan(val,uname):
    global amount
    mydb,my = db()
    amount,id,code=val.split(',')
    my.execute("select id from qr_code")
    for i in my:
        id_list=list(i)
    if id in id_list:
        my.execute(f"select status from qr_code where id ={id}")
        for i in my:
            for j in i:
                status=j
        if status==0:
            my.execute(f"select coins from auth where name='{uname}'")
            for k in my:
                for m in i:
                    coins=int(amount)+int(m)
            my.execute(f"update auth set coins={coins} where name='{uname}'")
            my.execute(f"update qr_code set status=1 where id ={id}")
            mydb.commit()
            return 'Qr successfully redeemed'
        else:
            return 'QR already redeemed'
    else:
        return 'QR not found'

def balance(uname):
    mydb,my = db()
    my.execute(f"select coins from auth where name='{uname}'")
    for i in my:
        for j in i:
            coins=j
    return coins


@app.route('/')
@app.route('/home')
def home():
    uname = request.cookies.get('username')
    pwd = request.cookies.get('password')
    print(uname,pwd)
    status = Login(uname,pwd)
    if status == 1:
        return render_template('index.html')
    else:
        return render_template('login.html')
    

@app.route('/login',methods=["POST","GET"])
def login():
    if request.method=='POST':
        uname= request.form['uname']
        pwd = request.form['password']
        status = Login(uname,pwd)
        if status == 1:
            resp = make_response(render_template('index.html'))
            resp.set_cookie('username',uname)
            resp.set_cookie('password',pwd)
            return resp
        else:
            return render_template('login.html',status=status)
    else:
        return home()
    
@app.route('/register',methods=["POST","GET"])
def register():
    if request.method=='POST':
        uname=request.form['uname']
        email=request.form['email']
        pwd=request.form['pwd']
        status = Register(uname,email,pwd)
        if status == 1:
            resp = make_response(render_template('index.html'))
            resp.set_cookie('username',uname)
            resp.set_cookie('password',pwd)
            return resp
        else:
            return render_template('registration.html',status=status)
    else:
        return home()


@app.route('/scanner')
def scanner():
    db()
    global qr_status,amount
    if qr_status==-1:
        return render_template('scanner.html')
    else:
        if qr_status=='Qr successfully redeemed':
            qr_status=-1
            return render_template('reward-page.html',amount=amount)
        else:
            status=qr_status
            qr_status=-1
            return render_template('scanner.html',status=status)

@app.route('/scan', methods=['POST'])
def scan():
    uname = request.cookies.get('username')
    global qr_status
    image_data = request.json['image']
    image_bytes = base64.b64decode(image_data.split(',')[1])
    image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    qr_codes = cv2.QRCodeDetector().detectAndDecodeMulti(gray)
    if qr_codes:
        try:
            val=qr_codes[1][0]
            _,_,code=val.split(',')
            if code=='bt1':
                qr_status = qr_scan(val,uname)
                return jsonify({'qrCodeFound': True,})
            else:
                qr_status='Qr not found'
                return jsonify({'qrCodeFound': False,})
        except:
            return jsonify({'qrCodeFound': False,})
    
@app.route('/profile')
def profile():
    uname = request.cookies.get('username')
    return render_template('account-page.html',username=uname)

@app.route('/store',methods=['POST','GET'])
def store():
    if request.method=='POST':
        item = request.form['item']
        return render_template('purchase.html',item=item)
    return render_template('store.html')

@app.route('/order')
def order():
    return render_template('order-conform.html')

@app.route('/earnings')
def earnings():
    uname = request.cookies.get('username')
    coins = balance(uname)
    return render_template('earnings.html',amount=coins)


if __name__=="__main__":
    app.run(port=34,debug=True)
