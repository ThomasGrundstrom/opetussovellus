import secrets
import users
import exams
from app import app
from app import db
from flask import render_template, redirect, request, session, abort


@app.route("/")
def index():
    teacher = users.is_teacher(db)
    allexams = exams.display_exams(db)
    return render_template("index.html", exams=allexams, is_teacher=teacher)

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    
    if users.login(db, username, password):
        session["username"] = username
        session["user_id"] = users.get_user_id(db, username)
        session["csrf_token"] = secrets.token_hex(16)
        return redirect("/")
    
    return render_template("index.html", errormessage = "Wrong username or password.")

@app.route("/logout")
def logout():
    del session["username"]
    del session["user_id"]
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
        session["user_id"] = users.get_user_id(db, username)
        session["csrf_token"] = secrets.token_hex(16)
        return redirect("/")
    
    return render_template("register.html", errormessage = "Username already in use.")

@app.route("/new", methods=["GET"])
def new_get():
    return render_template("new.html")

@app.route("/new", methods=["POST"])
def new_post():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    course = request.form["course"]
    topic = request.form["topic"]

    if exams.add_exam(db, course, topic):
        exam_id = exams.get_exam_id_by_topic(db, topic)
        session["exam"] = exam_id[0]
        return redirect("/add")
    
    return render_template("new.html", errormessage = "An exam with that topic already exists. Please change topic.")

@app.route("/add", methods=["GET"])
def add_get():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def add_post():
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    exam_id = session["exam"]
    question = request.form["question"]
    answer = request.form["answer"]
    exams.add_question_to_exam(db, exam_id, question, answer)
    return redirect("/add")

@app.route("/exam/<int:id>")
def exam(id):
    course = exams.get_exam_course(db, id)
    topic = exams.get_exam_topic(db, id)
    first_question = exams.get_next_question(db, id, session["user_id"])
    return render_template("exam.html", exam_course=course, exam_topic=topic, question=first_question, exam_id=id)
    

@app.route("/question/<int:exam_id>/<int:id>")
def question(exam_id, id):
    question = exams.get_question(db, id)
    return render_template("question.html", question=question, exam_id=exam_id)

@app.route("/question/<int:exam_id>/answer", methods=["POST"])
def answer_post(exam_id):
    if session["csrf_token"] != request.form["csrf_token"]:
        abort(403)
    answer = request.form["answer"]
    question = request.form["question"]
    question_id = request.form["question_id"]
    exams.answer_question(db, question_id, session["user_id"], answer)
    right_answer = exams.get_right_answer(db, question_id)
    next_question = exams.get_next_question(db, exam_id, session["user_id"])

    return render_template("answer.html", answer=answer, right_answer=right_answer, next_question=next_question, exam_id=exam_id)
