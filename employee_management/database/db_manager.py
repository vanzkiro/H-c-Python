import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'employee_management.db')

def get_connection():
    return sqlite3.connect(DB_PATH)

def initialize_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL,
            base_salary REAL NOT NULL,
            department TEXT,
            role TEXT NOT NULL,
            extra_info TEXT DEFAULT '',
            performance_score REAL DEFAULT 0.0
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS salaries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_id TEXT NOT NULL,
            calculated_salary REAL NOT NULL,
            month TEXT NOT NULL,
            FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS project_assignments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_id TEXT NOT NULL,
            project_name TEXT NOT NULL,
            assigned_date TEXT NOT NULL,
            FOREIGN KEY (emp_id) REFERENCES employees(emp_id)
        )
    """)

    conn.commit()
    conn.close()
