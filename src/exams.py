from sqlalchemy.sql import text

def display_exams(db):
    sql = text("SELECT id, course, topic FROM exams ORDER BY id DESC")
    result = db.session.execute(sql)
    return result.fetchall()

def add_exam(db, course, topic):
    if get_exam_id(db, topic):
        return False

    sql = text("INSERT INTO exams (course, topic) VALUES (:course, :topic)")
    db.session.execute(sql, {"course":course, "topic":topic})
    db.session.commit()
    return True

def get_exam_id(db, topic):
    sql = text("SELECT id FROM exams WHERE topic=:topic")
    result = db.session.execute(sql, {"topic":topic})
    return result.fetchone()

def add_question_to_exam(db, exam_id, question, answer, done):
    sql = text("INSERT INTO questions (exam_id, question, answer, done) VALUES (:exam_id, :question, :answer, :done)")
    db.session.execute(sql, {"exam_id":exam_id, "question":question, "answer":answer, "done":done})
    db.session.commit()

def get_exam_questions(db, exam_id, done):
    sql = text("SELECT id, question FROM questions WHERE exam_id=:exam_id AND done=:done")
    result = db.session.execute(sql, {"exam_id":exam_id, "done":done})
    return result.fetchall()

def get_exam_course(db, exam_id):
    sql = sql = text("SELECT course FROM exams WHERE id=:exam_id")
    result = db.session.execute(sql, {"exam_id":exam_id})
    return result.fetchone()[0]

def get_exam_topic(db, exam_id):
    sql = text("SELECT topic FROM exams WHERE id=:exam_id")
    result = db.session.execute(sql, {"exam_id":exam_id})
    return result.fetchone()[0]

def get_question(db, id):
    sql = text("SELECT question FROM questions WHERE id=:id")
    result = db.session.execute(sql, {"id":id})
    return result.fetchone()[0]