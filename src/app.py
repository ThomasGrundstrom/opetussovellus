import users
import exams
from flask import Flask, render_template, redirect, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")
db = SQLAlchemy(app)
app.secret_key = getenv("SECRET_KEY")

@app.route("/")
def index():
    allexams = exams.display_exams(db)
    return render_template("index.html", exams=allexams)

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    
    if users.login(db, username, password):
        session["username"] = username
        if users.is_teacher(db, username):
            session["teacher"] = 1 
        return redirect("/")
    
    return render_template("index.html", errormessage = "Wrong username or password.")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/register", methods=["GET"])
def register_get():
    return render_template("register.html")

@app.route("/register", methods=["POST"])
def register_post():
    username = request.form["username"]
    password1 = request.form["password1"]
    password2 = request.form["password2"]
    if request.form.get(str("teacher")) == "on":
        teacher = 1
    else:
        teacher = 0

    if password1 != password2:
        return render_template("register.html", errormessage = "Password and password confirmation do not match.")
    
    if users.register(db, username, password1, teacher):
        session["username"] = username
        if teacher == 1:
            session["teacher"] = teacher
        return redirect("/")
    
    return render_template("register.html", errormessage = "Username already in use.")

@app.route("/new", methods=["GET"])
def new_get():
    return render_template("new.html")

@app.route("/new", methods=["POST"])
def new_post():
    course = request.form["course"]
    topic = request.form["topic"]

    if exams.add_exam(db, course, topic):
        exam_id = exams.get_exam_id(db, topic)
        session["exam"] = exam_id[0]
        return render_template("add.html", exam_id=exam_id)
    
    return render_template("new.html", errormessage = "An exam with that topic already exists. Please change topic.")

@app.route("/add", methods=["GET"])
def add_get():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def add_post():
    exam_id = session["exam"]
    question = request.form["question"]
    answer = request.form["answer"]
    exams.add_question_to_exam(db, exam_id, question, answer)
    return redirect("/add")