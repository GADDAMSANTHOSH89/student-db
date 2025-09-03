-- Drops any existing table, then creates a fresh students table
DROP TABLE IF EXISTS students;

CREATE TABLE students (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    name  TEXT    NOT NULL,
    age   INTEGER NOT NULL,
    major TEXT
);