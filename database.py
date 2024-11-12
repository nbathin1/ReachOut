import sqlite3

def init_db():
    conn = sqlite3.connect('applications.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS job_applications (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            recruiter_name TEXT,
            email TEXT,
            date_applied TEXT,
            followup_prompt TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_application(recruiter_name, email, date_applied, followup_prompt):
    conn = sqlite3.connect('applications.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO job_applications (recruiter_name, email, date_applied, followup_prompt) VALUES (?, ?, ?, ?)',
                   (recruiter_name, email, date_applied, followup_prompt))
    conn.commit()
    conn.close()

def get_all_applications():
    conn = sqlite3.connect('applications.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM job_applications')
    rows = cursor.fetchall()
    conn.close()
    return rows

init_db()
