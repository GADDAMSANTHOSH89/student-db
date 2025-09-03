import sqlite3
import sys

import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, 'students.db')

menu = '''
Student Database Menu:
1. Add student
2. List students
3. Update student
4. Delete student
5. Exit
Choose an option (1-5): '''

def connect_db():
    return sqlite3.connect(DB_FILE)

def initialize():
    """Creates the database file and students table."""
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)
    print(f"[DEBUG] Using database file: {DB_FILE}")
    conn = connect_db()
    schema_path = os.path.join(BASE_DIR, 'schema.sql')
    print(f"[DEBUG] Using schema file: {schema_path}")
    with open(schema_path, 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database initialized.\n")

    # Check if students table exists
    conn = connect_db()
    try:
        conn.execute('SELECT 1 FROM students LIMIT 1')
        print("[DEBUG] Table 'students' exists and is accessible.")
    except sqlite3.OperationalError as e:
        print(f"[ERROR] Table 'students' does not exist or is not accessible: {e}")
    finally:
        conn.close()

def add_student():
    name  = input('Name: ').strip()
    age   = input('Age: ').strip()
    major = input('Major (optional): ').strip() or None
    conn = connect_db()
    conn.execute(
        'INSERT INTO students (name, age, major) VALUES (?, ?, ?)',
        (name, age, major)
    )
    conn.commit()
    conn.close()
    print('Student added.\n')

def list_students():
    conn   = connect_db()
    cursor = conn.execute('SELECT id, name, age, major FROM students')
    print('\nID | Name               | Age | Major')
    print('---+--------------------+-----+----------------')
    for row in cursor.fetchall():
        print(f"{row[0]:<3}| {row[1]:<18}| {row[2]:<3}| {row[3] or '-'}")
    print()
    conn.close()

def update_student():
    sid   = input('Enter student ID to update: ').strip()
    name  = input('New name (leave blank to skip): ').strip()
    age   = input('New age (leave blank to skip): ').strip()
    major = input('New major (leave blank to skip): ').strip()

    fields, params = [], []
    if name:
        fields.append('name = ?');  params.append(name)
    if age:
        fields.append('age = ?');   params.append(age)
    if major:
        fields.append('major = ?'); params.append(major)

    if not fields:
        print('No changes specified.\n')
        return

    params.append(sid)
    sql = f"UPDATE students SET {', '.join(fields)} WHERE id = ?"
    conn = connect_db()
    conn.execute(sql, params)
    conn.commit()
    conn.close()
    print('Student updated.\n')

def delete_student():
    sid = input('Enter student ID to delete: ').strip()
    conn = connect_db()
    conn.execute('DELETE FROM students WHERE id = ?', (sid,))
    conn.commit()
    conn.close()
    print('Student deleted.\n')

def main():
    initialize()
    while True:
        choice = input(menu).strip()
        if   choice == '1': add_student()
        elif choice == '2': list_students()
        elif choice == '3': update_student()
        elif choice == '4': delete_student()
        elif choice == '5':
            print('Exiting. Goodbye!')
            sys.exit(0)
        else:
            print('Invalid choice, try again.\n')

if __name__ == '__main__':
    main()
