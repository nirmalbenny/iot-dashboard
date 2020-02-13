from app import app
from app.models import User,Loglist
from app import db
from flask import render_template,redirect,request,url_for
from flask import jsonify
import datetime
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/add-user')
def addUser():
    return render_template('form.html')

@app.route('/addurl',methods=["GET","POST"])
def addurl():
    try:
        print("stage 1*")
        if request.method == 'POST':
            print('stage 2*')
            print(request.form)
            uid=request.form['uid']
            name=request.form['name']
            passcode=request.form['passcode']
            print("NAME {} | uid {} |  passcode {} |".format(name,uid,passcode))

            u=User(name=name, uid=uid,passcode=passcode)
            db.session.add(u)
            db.session.commit()
            users = User.query.all()
            for u in users:
                print(u.name)

            print("NAME {} | uid {} |  passcode {} |".format(name,uid,passcode))
            return jsonify({"status" : "success"})
        else:
            print("Invalid requests")
            return jsonify({"status" : "invalid request"})
    except Exception as e:
        print(e)
        return redirect('index')
#-------------------------------------VALIDATE API---------------------------------------
@app.route('/validate',methods=["POST","GET"])
def validate():
    if request.method == "POST":
        re={}
        users =User.query.filter_by(uid=request.form['uid']).first()
        if users is None:
            re={"valid" : "false", "passcode" : "Denied"}
            return jsonify(re)
        else:
            re={"valid" : "true", "passcode" : users.passcode}
            return jsonify(re)
@app.route('/sentlog',methods=["POST","GET"])
def sentlog():
    if request.method == "POST":
        l=Loglist(uid=request.form['uid'],name=request.form['name'],location=request.form['location'],date=datetime.datetime.utcnow())
        db.session.add(l)
        db.session.commit()
        print("______________LOG_______________")
        print(l.uid+" "+l.name+" ")
        return jsonify({"status" : "success"})

@app.route('/userslist')
def printlog():
    ul= User.query.all()
    d={}
    for e in ul:
        d.update({e.uid:{"name":e.name,"passcode":e.passcode}})
    print(d)
    return jsonify(d)

@app.route('/blocklist')
def blocklist():
    return render_template('blocklist.html')
@app.route('/loglist')
def loglist():
    l=Loglist.query.all()   
    return render_template('log.html',llist=l)
