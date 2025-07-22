📝 Student Database Management App
A lightweight, console‑based Student Database application built with Python and SQLite.
Perform essential CRUD operations on student records through an intuitive text‑menu interface.

🚀 Features
➕ Add students instantly (name, age, major)
🔍 View all students in a neatly formatted table
✏️ Update student details dynamically (one or more fields)
🗑️ Delete students by ID
💡 Input validation and user‑friendly menu navigation

🎯 Technologies Used

Technology	Role
Python 3.x	Core programming language
sqlite3	Built‑in module for SQLite integration
SQL	Database schema and CRUD queries
Text I/O	input() and console printing for UI

🛠️ How to Run

📥 Prerequisites

Python 3.x installed on your machine

No additional libraries required

▶️ Run Instructions

Clone or download this repo:

bash
Copy
Edit
git clone https://github.com/your‑username/student-db-demo.git
cd student-db-demo
Initialize and launch the app:

bash
Copy
Edit
python main.py
Follow the on‑screen menu to add, list, update, or delete student records.

🔍 How It Works

Database Initialization

On first run, schema.sql is executed to create the students table.

Adding Records

Prompts for Name, Age, and optional Major, then inserts into SQLite.

Viewing Records

Executes a SELECT query and prints results in columns: ID, Name, Age, Major.

Updating Records

Asks for student ID, then new values (skipping blanks), building a dynamic UPDATE statement.

Deleting Records

Removes a student row by ID with a DELETE statement.

📁 Project Structure

pgsql
Copy
Edit
student_db_project/
├── schema.sql      # SQL script to create ‘students’ table
└── main.py         # Python CLI app implementing CRUD menu
