CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT,
    password TEXT,
    teacher INTEGER
);

CREATE TABLE exams (
    id SERIAL PRIMARY KEY,
    course TEXT,
    topic TEXT
);

CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    exam_id INTEGER REFERENCES exams ON DELETE CASCADE,
    question TEXT
);

CREATE TABLE right_answers (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions ON DELETE CASCADE,
    right_answer TEXT
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions ON DELETE CASCADE,
    user_id INTEGER REFERENCES users ON DELETE CASCADE,
    answer TEXT
);
