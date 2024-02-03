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

def add_question_to_exam(db, exam_id, question, answer):
    sql = text("INSERT INTO questions (exam_id, question, answer) VALUES (:exam_id, :question, :answer)")
    db.session.execute(sql, {"exam_id":exam_id, "question":question, "answer":answer})
    db.session.commit()