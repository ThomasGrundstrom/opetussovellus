from sqlalchemy.sql import text


def display_exams(db):
    sql = text("SELECT id, course, topic, creator_id FROM exams ORDER BY id DESC")
    result = db.session.execute(sql)
    return result.fetchall()


def add_exam(db, course, topic, user_id):
    if get_exam_id_by_topic(db, topic):
        return False

    sql = text(
        "INSERT INTO exams (course, topic, creator_id) VALUES (:course, :topic, :creator_id)")
    db.session.execute(
        sql, {"course": course, "topic": topic, "creator_id": user_id})
    db.session.commit()
    return True


def get_exam_id_by_topic(db, topic):
    sql = text("SELECT id FROM exams WHERE topic=:topic")
    result = db.session.execute(sql, {"topic": topic})
    return result.fetchone()


def add_question_to_exam(db, exam_id, question, answer):
    sql = text(
        "INSERT INTO questions (exam_id, question) VALUES (:exam_id, :question)")
    db.session.execute(sql, {"exam_id": exam_id, "question": question})
    db.session.commit()
    sql = text("SELECT MAX(id) FROM questions")
    result = db.session.execute(sql)
    question_id = result.fetchone()[0]
    sql = text(
        "INSERT INTO right_answers (question_id, right_answer) VALUES (:question_id, :right_answer)")
    db.session.execute(
        sql, {"question_id": question_id, "right_answer": answer})
    db.session.commit()


def get_exam_questions(db, exam_id):
    sql = text("SELECT id, question FROM questions WHERE exam_id=:exam_id")
    result = db.session.execute(sql, {"exam_id": exam_id})
    return result.fetchall()


def get_exam_course(db, exam_id):
    sql = sql = text("SELECT course FROM exams WHERE id=:exam_id")
    result = db.session.execute(sql, {"exam_id": exam_id})
    return result.fetchone()[0]


def get_exam_topic(db, exam_id):
    sql = text("SELECT topic FROM exams WHERE id=:exam_id")
    result = db.session.execute(sql, {"exam_id": exam_id})
    return result.fetchone()[0]


def get_question(db, id):
    sql = text("SELECT id, question FROM questions WHERE id=:id")
    result = db.session.execute(sql, {"id": id})
    return result.fetchone()


def get_right_answer(db, question_id):
    sql = text(
        "SELECT right_answer FROM right_answers WHERE question_id=:question_id")
    result = db.session.execute(sql, {"question_id": question_id})
    return result.fetchone()[0]


def answer_question(db, question_id, user_id, answer):
    sql = text(
        "INSERT INTO answers (question_id, user_id, answer) VALUES (:question_id, :user_id, :answer)")
    db.session.execute(sql, {"question_id": question_id,
                       "user_id": user_id, "answer": answer})
    db.session.commit()


def get_next_question(db, exam_id, user_id):
    allquestions = get_exam_questions(db, exam_id)
    sql = text("SELECT question_id FROM answers WHERE user_id=:user_id")
    answers = db.session.execute(sql, {"user_id": user_id}).fetchall()
    questions = []
    unanswered = True
    for i in range(len(allquestions)):
        for j in range(len(answers)):
            if allquestions[i][0] == answers[j][0]:
                unanswered = False
        if unanswered:
            questions.append(allquestions[i])
        unanswered = True
    if len(questions) != 0:
        return questions[0]
    return None


def get_exam_results(db, exam_id, user_id):
    sql = text("SELECT q.question, a.answer, r.right_answer FROM questions q, answers a, right_answers r WHERE q.exam_id=:exam_id AND a.question_id=q.id AND a.user_id=:user_id AND r.question_id=q.id")
    result = db.session.execute(sql, {"exam_id": exam_id, "user_id": user_id})
    return result.fetchall()


def get_exam_takers(db, exam_id):
    sql = text("SELECT DISTINCT(u.username) FROM users u, questions q, answers a WHERE q.exam_id=:exam_id AND a.question_id=q.id AND a.user_id=u.id")
    result = db.session.execute(sql, {"exam_id": exam_id})
    return result.fetchall()


def remove_exam_answers(db, exam_id, user_id):
    questions = get_exam_questions(db, exam_id)
    for question in questions:
        question_id = question[0]
        sql = text(
            "DELETE FROM answers WHERE question_id=:question_id AND user_id=:user_id")
        db.session.execute(
            sql, {"question_id": question_id, "user_id": user_id})
        db.session.commit()


def delete_exam(db, exam_id):
    sql = text("DELETE FROM exams WHERE id=:exam_id")
    db.session.execute(sql, {"exam_id": exam_id})
    db.session.commit()


def get_exam_creator(db, exam_id):
    sql = text("SELECT creator_id FROM exams WHERE id=:exam_id")
    result = db.session.execute(sql, {"exam_id": exam_id})
    return result.fetchone()[0]
