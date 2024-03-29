from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash
from flask import session


def register(db, username, password, teacher=0):

    if find_existing_user(db, username):
        return False

    hash_value = generate_password_hash(password)
    sql = text(
        "INSERT INTO users (username, password, teacher) VALUES (:username, :password, :teacher)")
    db.session.execute(
        sql, {"username": username, "password": hash_value, "teacher": teacher})
    db.session.commit()

    return True


def find_existing_user(db, username):
    sql = text("SELECT * FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()

    if user:
        return True

    return False


def login(db, username, password):

    if find_existing_user(db, username):
        sql = text("SELECT id, password FROM users WHERE username=:username")
        result = db.session.execute(sql, {"username": username})
        user = result.fetchone()

        if check_password_hash(user.password, password):
            return True

    return False


def is_teacher(db):
    username = session.get("username")
    sql = text("SELECT teacher FROM users WHERE username=:username AND teacher=1")
    result = db.session.execute(sql, {"username": username}).fetchone()

    if result:
        return True

    return False


def get_user_id(db, username):
    sql = text("SELECT id FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    return result.fetchone()[0]
