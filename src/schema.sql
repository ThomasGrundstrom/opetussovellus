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
    exam_id INTEGER REFERENCES exams,
    question TEXT,
    answer TEXT, 
    done INTEGER
);

CREATE TABLE answers (
    id SERIAL PRIMARY KEY,
    question_id INTEGER REFERENCES questions,
    answer TEXT
);
