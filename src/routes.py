import users
import exams
from app import app
from app import db
from flask import render_template, redirect, request, session


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
        exam_id = exams.get_exam_id_by_topic(db, topic)
        session["exam"] = exam_id[0]
        return redirect("/add")
    
    return render_template("new.html", errormessage = "An exam with that topic already exists. Please change topic.")

@app.route("/add", methods=["GET"])
def add_get():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def add_post():
    exam_id = session["exam"]
    question = request.form["question"]
    answer = request.form["answer"]
    exams.add_question_to_exam(db, exam_id, question, answer, done=0)
    return redirect("/add")

@app.route("/exam/<int:id>")
def exam(id):
    course = exams.get_exam_course(db, id)
    topic = exams.get_exam_topic(db, id)
    questions = exams.get_exam_questions(db, id, done=0)

    if len(questions) != 0:
        first_question = questions[0]
        return render_template("exam.html", exam_course=course, exam_topic=topic, question=first_question)
    
    return "Exam complete!"

@app.route("/question/<int:id>")
def question(id):
    question = exams.get_question(db, id)
    return render_template("question.html", question=question)

@app.route("/question/answer", methods=["POST"])
def answer_post():
    answer = request.form["answer"]
    question = request.form["question"]
    exams.mark_question_as_done(db, question)
    right_answer = exams.get_right_answer(db, question)
    exam_id = exams.get_exam_id_by_question(db, question)
    remaining_questions = exams.get_exam_questions(db, exam_id, done=0)

    if len(remaining_questions) != 0:
        next_question = remaining_questions[0]
        return render_template("answer.html", answer=answer, right_answer=right_answer, next_question=next_question)
    
    return "Exam complete!"