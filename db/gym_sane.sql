-- Deleting the tables in reverse order to creation
DROP TABLE IF EXISTS bookings;
DROP TABLE IF EXISTS sessions;
DROP TABLE IF EXISTS members;

-- Members table created with the first name, last name, age and category
CREATE TABLE members (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    category VARCHAR(255)
);

-- Sessions table created with name, time and category
CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    time VARCHAR(255),
    category VARCHAR(255)
);

-- Attendance table created to link the members and classes tables
CREATE TABLE bookings (
    id SERIAL PRIMARY KEY,
    member_id INT REFERENCES members(id) ON DELETE CASCADE,
    session_id INT REFERENCES sessions(id) ON DELETE CASCADE
);