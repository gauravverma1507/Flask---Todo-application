from flask import Flask, redirect,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#CONFIGURATION OF DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
db = SQLAlchemy(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#MAKING A CLASS FOR TODO    

class Todo(db.Model):
    sno = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(200), nullable = False)
    desc = db.Column(db.String(500), nullable = False)
    date_created = db.Column(db.DateTime, default= datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno}-{self.title}"

@app.route("/" , methods = ['GET','POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title,desc = desc)
        db.session.add(todo)
        db.session.commit()
    allTodo =  Todo.query.all()
    return render_template('index.html',allTodo=allTodo)

@app.route("/about")
def products():
    alltodo = Todo.query.all()
    print(alltodo)
    return "THIS IS AN WEB APPLICATION WHICH IS WRITTEN IN PYTHON AND DEPLOYED ON HEROKU ,NOW JUST USE THIS APPLICATION SO THAT YOU WILL NOT FORGOT YOU DAILY BASIS TASKS"

@app.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route("/home")
def home():
    alltodo = Todo.query.all()
    print(alltodo)
    return redirect("/")        

if __name__ == "__main__"    :
    app.run(debug=True)