DROP TABLE IF EXISTS attendance;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS members;

CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    category VARCHAR(255)
);

CREATE TABLE classes (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    time VARCHAR(255),
    category VARCHAR(255)
);

CREATE TABLE attendance (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    class_id INT REFERENCES classes(id) ON DELETE CASCADE
);