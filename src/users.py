from sqlalchemy.sql import text
from werkzeug.security import check_password_hash, generate_password_hash

def register(db, username, password):

    if find_existing_user(db, username):
        return False
    
    hash_value = generate_password_hash(password)
    sql = text("INSERT INTO users (username, password) VALUES (:username, :password)")
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()

    return True

def find_existing_user(db, username):
    sql = text("SELECT * FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if user:
        return True
    
    return False

def login(db, username, password):

    if not find_existing_user(db, username):
        return False
    
    sql = text("SELECT id, password FROM users WHERE username=:username")
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()

    if not check_password_hash(user.password, password):
        return False
    
    return True