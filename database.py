import sqlite3

conn = sqlite3.connect('employees.db')

c = conn.cursor()
c.execute('''CREATE TABLE employee
             (EmpID INTEGER PRIMARY KEY,
             EmpName TEXT,
             EmpGender TEXT,
             EmpPhone TEXT,
             EmpBdate TEXT)''')
conn.commit()

conn.close()

